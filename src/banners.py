"""Generate full-width banners with baked-in headline + CTA (landscape + portrait)."""
import io, os, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from data import U, BANNERS

FDIR = '/usr/share/fonts/truetype/google-fonts/'
F_BOLD = FDIR + 'Poppins-Bold.ttf'
F_SEMI = FDIR + 'Poppins-Bold.ttf'
F_MED = FDIR + 'Poppins-Medium.ttf'

SPEC = {  # key: (eyebrow, headline lines, cta, focal-x fraction)
 'women': ('WOMEN · BOTTOMWEAR', ['ONE FIT YOU WILL', 'REORDER IN SIX', 'COLOURS'], 'Shop Women', .62),
 'men':   ('MEN · NEW AT GO COLORS', ['EVERYDAY TAILORING,', 'BUILT FOR THE', 'COMMUTE'], 'Shop Men', .60),
 'girls': ('GIRLS · 6 TO 14 YEARS', ['SCHOOL, PLAY AND', 'EVERYTHING AFTER'], 'Shop Girls', .58),
}
CACHE = '/root/gocolors/.bancache'


def fetch(url):
    os.makedirs(CACHE, exist_ok=True)
    fp = os.path.join(CACHE, url.rsplit('/', 1)[-1].split('?')[0])
    if not os.path.exists(fp):
        rq = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(rq, timeout=60) as r, open(fp, 'wb') as f:
            f.write(r.read())
    return Image.open(fp).convert('RGB')


def cover(im, w, h, fx=.5, fy=.42):
    r = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * r)), max(h, int(im.height * r))), Image.LANCZOS)
    x = int((im.width - w) * fx)
    y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def scrim(im, side_frac, dark=.72, horizontal=True):
    w, h = im.size
    g = Image.new('L', (w, h), 0)
    d = ImageDraw.Draw(g)
    if horizontal:
        span = int(w * side_frac)
        for x in range(span):
            d.line([(x, 0), (x, h)], fill=int(255 * dark * (1 - (x / span) ** 1.5)))
    else:
        span = int(h * side_frac)
        for y in range(h - span, h):
            t = (y - (h - span)) / span
            d.line([(0, y), (w, y)], fill=int(255 * dark * (t ** .8)))
    black = Image.new('RGB', (w, h), (12, 16, 10))
    return Image.composite(black, im, g.filter(ImageFilter.GaussianBlur(2)))


def draw_copy(im, eyebrow, lines, cta, box, scale, fill=(255, 255, 255),
              cta_bg=(255, 255, 255), cta_fg=(17, 17, 17)):
    d = ImageDraw.Draw(im)
    x, y = box
    fe = ImageFont.truetype(F_MED, int(20 * scale))
    fh = ImageFont.truetype(F_BOLD, int(58 * scale))
    fc = ImageFont.truetype(F_SEMI, int(24 * scale))
    d.text((x, y), eyebrow, font=fe, fill=fill, spacing=0)
    y += int(40 * scale)
    for ln in lines:
        d.text((x, y), ln, font=fh, fill=fill)
        y += int(70 * scale)
    y += int(18 * scale)
    tw = d.textlength(cta, font=fc)
    pad_x, pad_y = int(30 * scale), int(15 * scale)
    bw, bh = int(tw) + pad_x * 2, int(34 * scale) + pad_y * 2
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=bh // 2, fill=cta_bg)
    d.text((x + pad_x, y + pad_y - int(4 * scale)), cta, font=fc, fill=cta_fg)
    return im


BG = {'women': (241, 233, 236), 'men': (226, 231, 236), 'girls': (243, 236, 228)}
INK = (26, 26, 26)


def fade_left(im, frac=.16):
    """Soften the photo's left edge into the colour field."""
    w, h = im.size
    m = Image.new('L', (w, h), 255)
    d = ImageDraw.Draw(m)
    span = int(w * frac)
    for x in range(span):
        d.line([(x, 0), (x, h)], fill=int(255 * (x / span) ** .9))
    return m


def compose(src, size, key, eyebrow, lines, cta, portrait=False):
    W, H = size
    canvas = Image.new('RGB', (W, H), BG[key])
    if portrait:
        ph = int(H * .58)
        photo = cover(src, W, ph, fx=.5, fy=.03)
        canvas.paste(photo, (0, 0))
        scale = H / 1200.0
        draw_copy(canvas, eyebrow, lines, cta, (int(W * .07), ph + int(70 * scale)),
                  1.02 * scale, INK, cta_bg=INK, cta_fg=(255, 255, 255))
    else:
        pw = int(W * .52)
        photo = cover(src, pw, H, fx=.5, fy=.10)
        canvas.paste(photo, (W - pw, 0), fade_left(photo))
        scale = H / 758.0
        block = int(len(lines) * 70 + 130) * scale
        draw_copy(canvas, eyebrow, lines, cta, (int(W * .06), int((H - block) / 2)),
                  1.5 * scale, INK, cta_bg=INK, cta_fg=(255, 255, 255))
    return canvas


def build(outdir):
    os.makedirs(outdir, exist_ok=True)
    made = {}
    # home: the live Go Colors campaign key visual (already carries copy + CTA)
    for tag, url, size in [
        ('lg', 'https://gocolors.com/cdn/shop/files/Website_Banner_-_SK-KV2.jpg', (2400, 758)),
        ('sm', 'https://gocolors.com/cdn/shop/files/Website_Banner_-_SK-KV2_600_x_800.jpg', (900, 1200))]:
        im = fetch(url)
        im = cover(im, *size, fx=.5, fy=.5)
        fn = 'home-%s.jpg' % tag
        im.save(os.path.join(outdir, fn), quality=88, optimize=True)
        made.setdefault('home', {})[tag] = 'banners/' + fn

    for key, (eyebrow, lines, cta, fx) in SPEC.items():
        src = fetch(U(BANNERS[key][8]))
        lg = compose(src, (2400, 758), key, eyebrow, lines, cta)
        sm = compose(src, (900, 1200), key, eyebrow, lines, cta, portrait=True)
        for tag, im in (('lg', lg), ('sm', sm)):
            fn = '%s-%s.jpg' % (key, tag)
            im.save(os.path.join(outdir, fn), quality=88, optimize=True)
            made.setdefault(key, {})[tag] = 'banners/' + fn
    return made


if __name__ == '__main__':
    print(build('/root/gocolors/gocolors-mockups/banners'))
