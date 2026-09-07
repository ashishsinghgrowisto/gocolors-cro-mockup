# -*- coding: utf-8 -*-
"""Go Colors — interactive static mockup generator (CRO-improved variant).

Images are referenced straight from the Shopify CDN, so the pages need a
network connection but stay byte-small and always show the live artwork.
"""
import os, sys, json, html, random, shutil, re, hashlib
from concurrent.futures import ThreadPoolExecutor

from data import (U, BRAND, ANNOUNCE, NAV, NAV_GROUPS, MEGA_PROMOS, SIZES_CHIPS, CAT_TABS,
                  PRICE_BANDS, SPOTLIGHT, PRODUCTS, COLOR_HEX, SHADES, REVIEWS,
                  FAQ, FOOTER, L1, BANNERS, CATEGORIES)
from style import CSS
from script import JS, JS_PLP, JS_PDP, JS_WISH

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gocolors-mockups')
E = html.escape
random.seed(11)

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800'
             '&display=swap" rel="stylesheet">')

# --------------------------------------------------------------- derived data
COLOUR_WORDS = sorted(COLOR_HEX, key=len, reverse=True)

def guess_colour(title):
    for c in COLOUR_WORDS:
        if c.lower() in title.lower():
            return c
    return ''

def derive(title, ptype, sizes):
    t = (title + ' ' + ptype).lower()
    whom = 'Girls' if 'girls' in t else 'Women'
    if any(k in t for k in ('ankle', 'capri', 'shorts', 'cropped', 'churidar')):
        length = 'Half Length'
    else:
        length = 'Full Length'
    if any(k in t for k in ('legging', 'jegging', 'skinny', 'churidar')):
        fit = 'Bodycon Fit'
    elif any(k in t for k in ('palazzo', 'wide', 'culotte', 'harem', 'cargo sweat')):
        fit = 'Baggy Fit'
    elif any(k in t for k in ('jogger', 'track', 'sweat')):
        fit = 'Relaxed Fit'
    elif 'tapered' in t or 'pencil' in t:
        fit = 'Slim Fit'
    else:
        fit = 'Regular Fit'
    if 'print' in t or 'ikat' in t:
        pattern = 'Printed'
    elif 'stripe' in t:
        pattern = 'Striped'
    elif 'shimmer' in t or 'metallic' in t:
        pattern = 'Shimmer'
    else:
        pattern = 'Solid'
    for key, lab in (('denim', 'Denim'), ('viscose', 'Viscose'), ('linen', 'Linen'),
                     ('nylon', 'Nylon'), ('velour', 'Velour'), ('lyocell', 'Lyocell'),
                     ('poly', 'Cotton & Polyester'), ('cotton', 'Cotton')):
        if key in t:
            fabric = lab
            break
    else:
        fabric = 'Cotton'
    if 'high rise' in t or 'yoga' in t:
        rise = 'High Rise'
    elif any(k in t for k in ('legging', 'churidar', 'jegging')):
        rise = 'Mid Rise'
    else:
        rise = 'Mid Rise'
    return whom, length, fit, pattern, fabric, rise

def build_products():
    out = []
    nudges = ['Bestseller in this fit', '', 'Low stock — few left', '',
              'Restocked this week', '', 'Loved for plus sizes', '']
    for i, p in enumerate(PRODUCTS):
        h, t, ty, pr, cp, imgs, sz, sw = p[:8]
        whom, length, fit, pattern, fabric, rise = derive(t, ty, sz)
        if len(p) > 8:                 # explicit audience wins over the guess
            whom = p[8]
        swatches = [[c, U(u), COLOR_HEX.get(c, '#cccccc')] for c, u in sw]
        cols = [c for c, _u, _x in swatches] or ([guess_colour(t)] if guess_colour(t) else [])
        out.append(dict(
            h=h, t=t, ty=ty, p=float(pr), cp=float(cp) if cp else 0,
            i=[U(x) for x in imgs], sz=sz, sw=swatches, cols=cols,
            whom=whom, len=length, fit=fit, pat=pattern, fab=fabric, rise=rise,
            r=round(random.uniform(4.1, 4.8), 1), rc=random.randint(64, 2140),
            nw=1 if i in (12, 14, 15) else 0, bs=1 if i in (0, 1, 6, 18) else 0,
            nudge=nudges[i % len(nudges)],
        ))
    return out

PROD = build_products()

# product rails: bestsellers / new arrivals / trending, per audience and overall.
# Proxies, since the catalogue carries no sales or publish dates:
#   bestseller = most reviewed   new = fewest reviews (newest listing)
#   trending   = highest rated among the rest
POOLS = {}
MIN_RAIL = 8

def _rails(pool):
    by_reviews = sorted(pool, key=lambda x: -x['rc'])
    best = by_reviews[:12]
    new = sorted(pool, key=lambda x: x['rc'])[:12]
    rest = [p for p in pool if p not in best] or pool
    trend = sorted(rest, key=lambda x: (-x['r'], -x['rc']))[:12]
    out = {'Bestsellers': best, 'New Arrivals': new, 'Trending Products': trend}
    for k, v in out.items():                      # never show a thin rail
        if len(v) < MIN_RAIL:
            extra = [p for p in by_reviews if p not in v]
            out[k] = (v + extra)[:MIN_RAIL]
    return out

for _a in ('Women', 'Men', 'Girls'):
    POOLS[_a] = _rails([p for p in PROD if p['whom'] == _a])
    for _p in POOLS[_a]['Bestsellers']:
        _p['bs'] = 1
    for _p in POOLS[_a]['New Arrivals']:
        _p['nw'] = 1
for _p in PROD:
    _p.setdefault('bs', 0)

def _interleave(key, n=12):
    """Homepage: across categories, one from each audience in turn."""
    out, i = [], 0
    while len(out) < n:
        added = False
        for a in ('Women', 'Men', 'Girls'):
            lst = POOLS[a][key]
            if i < len(lst):
                out.append(lst[i]); added = True
        if not added:
            break
        i += 1
    return out[:n]

POOLS['All'] = {k: _interleave(k) for k in ('Bestsellers', 'New Arrivals', 'Trending Products')}
BESTSELLERS = {a: POOLS[a]['Bestsellers'] for a in POOLS}   # kept for compatibility
BY = {p['h']: p for p in PROD}
DATA_JSON = json.dumps(PROD, ensure_ascii=False, separators=(',', ':'))
SHADE_JSON = json.dumps([[s, COLOR_HEX.get(s, '#ccc')] for s in SHADES])

def count_by(key):
    d = {}
    for p in PROD:
        d[p[key]] = d.get(p[key], 0) + 1
    return sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))

ALL_COLOURS = []
for p in PROD:
    for c in p['cols']:
        if c and c not in ALL_COLOURS:
            ALL_COLOURS.append(c)

# --------------------------------------------------------------- icons
IC = {
 'play': '<svg width="20" height="22" viewBox="0 0 24 26" aria-hidden="true"><path fill="#00D4FF" d="M2 1.4 13.6 13 2 24.6A2 2 0 0 1 1.2 23V3A2 2 0 0 1 2 1.4z"/><path fill="#FFCE00" d="m18.2 8.6 4 2.3c1.4.8 1.4 2.4 0 3.2l-4 2.3L14.6 13z"/><path fill="#FF3A44" d="M2 24.6 13.6 13l3.6 3.4-11.6 6.7c-1.4.8-2.6.6-3.6.5z"/><path fill="#00F076" d="M2 1.4 13.6 13l3.6-3.4L5.6 2.9C4.2 2.1 3 2.3 2 1.4z"/></svg>',
 'apple': '<svg width="19" height="22" viewBox="0 0 24 26" fill="currentColor" aria-hidden="true"><path d="M17.6 13.7c0-2.9 2.4-4.3 2.5-4.4-1.4-2-3.5-2.3-4.2-2.3-1.8-.2-3.5 1-4.4 1-.9 0-2.3-1-3.8-1C5.8 7 4 8.1 3 10c-2 3.5-.5 8.7 1.4 11.5.9 1.4 2 3 3.5 2.9 1.4-.1 1.9-.9 3.6-.9s2.2.9 3.7.9c1.5 0 2.5-1.4 3.4-2.8 1.1-1.6 1.5-3.2 1.5-3.3-.1 0-3-1.2-3-4.6zM14.8 4.9c.8-1 1.3-2.3 1.2-3.6-1.2 0-2.6.8-3.4 1.7-.7.8-1.4 2.2-1.2 3.5 1.3.1 2.6-.7 3.4-1.6z"/></svg>',
 'search': '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
 'user': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.5 20.5c0-3.8 3.4-6 7.5-6s7.5 2.2 7.5 6"/></svg>',
 'heart': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1L12 21l7.7-7.7 1.1-1a5.5 5.5 0 0 0 0-7.7z"/></svg>',
 'bag': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 7.5h14L20 21H4L5 7.5z"/><path d="M9 7.5V6a3 3 0 0 1 6 0v1.5"/></svg>',
 'store': '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 9.5 5 4.5h14l1.5 5"/><path d="M4.5 9.5V20h15V9.5"/><path d="M3.5 9.5a2.6 2.6 0 0 0 5.2 0 2.6 2.6 0 0 0 5.2 0 2.6 2.6 0 0 0 5.2 0"/></svg>',
 'menu': '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M3 6.5h18M3 12h18M3 17.5h18"/></svg>',
 'home': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V21h13V9.5"/></svg>',
 'truck': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 7h11v10H2z"/><path d="M13 10h4l4 3.5V17h-8z"/><circle cx="6" cy="18.5" r="1.7"/><circle cx="17" cy="18.5" r="1.7"/></svg>',
 'ret': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>',
 'cod': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/></svg>',
 'lock': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="10" width="15" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
 'mail': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="m3 6.5 9 6.5 9-6.5"/></svg>',
 'phone': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5c0 8.3 6.7 15 15 15l1.5-3.5-4-1.6-2 2A13.6 13.6 0 0 1 8.1 9.5l2-2L8.5 3.5 5 5z"/></svg>',
 'wa': '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a9 9 0 1 0-7.8-4.5L3 21l4.6-1.2A9 9 0 0 0 12 21z"/></svg>',
 'x': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 5l14 14M19 5 5 19"/></svg>',
 'arr': '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M17 7 7 17"/><path d="M17 16V7H8"/></svg>',
 'spark': '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.2 6.3L21 10l-6.8 1.7L12 18l-2.2-6.3L3 10l6.8-1.7z"/></svg>',
}

def logo(cls='logo'):
    return ('<a class="%s" href="home.html" aria-label="Go Colors home">'
            '<span class="lg">GO COLORS</span><span class="ex">!</span></a>' % cls)

def num():
    return ''

# --------------------------------------------------------------- chrome
def app_strip():
    return ('<div class="appstrip" id="appstrip">'
            '<span class="txt">🎉 Enjoy Seamless Shopping &amp; Faster Checkout</span>'
            '<a class="cta" href="#">Download The App</a>'
            '<button class="x" data-appclose aria-label="Dismiss">×</button></div>'
            '<div class="greenline"></div>')

NAV_IMG_FALLBACK = {}


def nav_thumb(audience, name):
    """Best-matching image for a menu link: category art first, then a product shot."""
    key = (audience, name)
    if key in NAV_IMG_FALLBACK:
        return NAV_IMG_FALLBACK[key]
    want = _toks(name)
    img = ''
    for title, cimg, _sale in CATEGORIES.get(audience, []):
        hay = ' '.join(_toks(title))
        if hay and any(w in hay or hay.split()[0] in _toks(name) for w in want):
            img = U(cimg)
            break
    if not img:
        pool = [p for p in PROD if p['whom'] == audience] or PROD
        for p in pool:
            hay = ' '.join(_toks(p['ty'] + ' ' + p['t']))
            if any(w in hay for w in want):
                img = p['i'][0]
                break
    if not img:
        cats = CATEGORIES.get(audience) or CATEGORIES['Women']
        img = U(cats[len(NAV_IMG_FALLBACK) % len(cats)][1])
    NAV_IMG_FALLBACK[key] = img
    return img


def mega(audience):
    cols = ''.join(
        '<div class="mcol"><div class="mhd">%s</div>%s</div>'
        % (E(group),
           ''.join('<a class="mlink" href="collection.html">'
                   '<img src="%s" alt="" loading="lazy">'
                   '<span>%s</span></a>' % (nav_thumb(audience, nm), E(nm))
                   for nm in links))
        for group, links in NAV_GROUPS[audience])
    promos = ''.join(
        '<a class="mega-promo" href="collection.html"><img src="%s" alt="%s" loading="lazy">'
        '<span class="cap">%s</span></a>' % (U(img), E(cap), E(cap))
        for img, cap in MEGA_PROMOS[:2])
    return ('<div class="mega"><div class="mega-in">'
            '<div class="mcols">%s</div>'
            '<div class="mega-side">'
            '<a class="allbtn" href="%s.html">Shop all %s \u203a</a>'
            '<div class="hd">Edits for you</div>%s'
            '</div></div></div>'
            % (cols, audience.lower(), E(audience), promos))


def header():
    navhtml = ''.join(
        '<li><span class="top">%s%s<i class="car">▾</i></span>%s</li>'
        % ('<i class="badge">NEW</i>' if label == 'Men' else '', E(label), mega(label))
        for label, _href, _kids in NAV)
    return (
      '<header class="hdr"><div class="hdr-in">'
      '<button class="burger" data-burger aria-label="Open menu">%s</button>'
      '%s'
      '<ul class="nav">%s</ul>'
      '<div class="searchbox" data-search><span class="si">%s</span>'
      '<input placeholder="Search for Leggings" readonly aria-label="Search"></div>'
      '<div class="icons">'
      '<a class="ico" href="#" title="Store locator">%s<span class="lbl">Stores</span></a>'
      '<a class="ico" href="#" title="Account">%s<span class="lbl">Account</span></a>'
      '<a class="ico" href="#" data-openwish title="Wishlist">%s'
      '<i class="cnt" data-wishcount style="display:none">0</i><span class="lbl">Wishlist</span></a>'
      '<a class="ico" href="#" data-opencart title="Bag">%s'
      '<i class="cnt" data-cartcount style="display:none">0</i><span class="lbl">Bag</span></a>'
      '</div></div></header>'
      % (IC['menu'], logo(), navhtml, IC['search'], IC['store'], IC['user'], IC['heart'], IC['bag']))

def drawer():
    """Mobile menu: audience pills, then every collection in the hierarchy."""
    auds = list(NAV_GROUPS.keys())
    pills = ''.join('<button data-mtab="%s" class="%s">%s%s</button>'
                    % (a, 'on' if i == 0 else '',
                       '<i class="badge">NEW</i>' if a == 'Men' else '', E(a))
                    for i, a in enumerate(auds))
    panels = ''
    for i, a in enumerate(auds):
        groups = ''.join(
            '<div class="dgrp"><div class="dhd">%s</div><div class="dgrid">%s</div></div>'
            % (E(group),
               ''.join('<a href="collection.html"><img src="%s" alt="" loading="lazy">'
                       '<span>%s</span></a>' % (nav_thumb(a, nm), E(nm))
                       for nm in links))
            for group, links in NAV_GROUPS[a])
        panels += ('<div class="dpanel" data-mpanel="%s" style="%s">'
                   '<a class="dall" href="%s.html">Shop all %s \u203a</a>%s'
                   '<div class="dpromo">%s</div></div>'
                   % (a, '' if i == 0 else 'display:none', a.lower(), E(a), groups,
                      ''.join('<a href="collection.html"><img src="%s" alt="%s" loading="lazy">'
                              '<span>%s</span></a>' % (U(img), E(cap), E(cap))
                              for img, cap in MEGA_PROMOS[:3])))
    links = ''.join('<a href="%s">%s <span>\u203a</span></a>' % (h, E(t)) for h, t in
                    [('home.html', 'Home'), ('collection.html', 'New Arrivals'),
                     ('collection.html', 'Best Sellers')])
    links += ''.join('<a href="#"%s>%s <span>\u203a</span></a>' % (x, E(t)) for x, t in
                     [(' data-openwish', 'Wishlist'), ('', 'Track my order'),
                      ('', 'Store locator'), ('', 'Go Rewards')])
    return ('<aside class="drw" id="navDrw">'
            '<div class="drw-hd">%s<button data-close aria-label="Close">%s</button></div>'
            '<div class="drw-pills">%s</div>'
            '<div class="drw-body">%s<div class="drw-links">%s</div></div>'
            '<div class="drw-foot"><span>Free shipping \u00b7 30-day returns \u00b7 Free COD</span>'
            '<span>customercare@gocolors.com \u00b7 1800-123-9953</span></div></aside>'
            % (logo(), IC['x'], pills, panels, links))


def search_overlay():
    cats = ['Leggings', 'Leggings and Churidar']
    trends = ['Leggings for women', 'Leggings for girls', 'Leggings &amp; Churidar for women',
              'Leggings &amp; Churidar for girls', 'Leggings &amp; Churidar Plus for women',
              'Leggings &amp; Churidar Plus for women in Bright Red',
              'Leggings &amp; Churidar Plus for women in Light Blue Denim',
              'Leggings &amp; Churidar Plus for women in Rust']
    rows = lambda items: ''.join(
        '<a class="row" href="collection.html"><span>%s</span><span class="ar">%s</span></a>'
        % (i, IC['arr']) for i in items)
    prods = ''.join(
        '<a href="product.html?p=%s"><img src="%s" alt="%s" loading="lazy">'
        '<div class="n">%s</div><div class="p">₹ %s</div></a>'
        % (p['h'], p['i'][0], E(p['t']), E(p['t']), '{:,}'.format(int(p['p'])))
        for p in PROD[:8])
    return ('<div class="srch" id="searchOvl">'
            '<div class="srch-top"><input id="searchInput" placeholder="Search for leggings" value="leggings">'
            '<button data-close aria-label="Close">%s</button></div>'
            '<div class="srch-in">'
            '<div class="hd">Categories</div>%s'
            '<div class="hd">Trending searches</div>%s'
            '<div class="hd">Top products</div><div class="srch-prods">%s</div>'
            '</div></div>' % (IC['x'], rows(cats), rows(trends), prods))

def cart_drawer():
    rail = ''.join(
        '<div data-quick="%s"><img src="%s" alt="%s" loading="lazy">'
        '<div class="p">%s</div><div class="a">+ Add</div></div>'
        % (p['h'], p['i'][0], E(p['t']), E(p['ty'])) for p in PROD[5:12])
    chips = ''.join('<div>%s<span>%s</span></div>' % (ic, lab) for ic, lab in
                    [(IC['truck'], 'Free<br>Delivery'), (IC['ret'], 'Easy<br>Returns'),
                     (IC['cod'], 'Cash on<br>Delivery')])
    return ('<aside class="side" id="cartDrw">'
            '<div class="side-hd"><button class="bk" data-close aria-label="Close">←</button>'
            '<h3>Shopping Bag</h3><span style="width:20px"></span></div>'
            '<div class="steps"><span class="s on"><i></i>Cart</span><span class="ln"></span>'
            '<span class="s"><i></i>Checkout</span><span class="ln"></span>'
            '<span class="s"><i></i>Payment</span></div>'
            '<div class="tchips">%s</div>'
            '<div class="ship"><div class="t" id="shipTxt"></div>'
            '<div class="bar"><i id="shipBar" style="width:0"></i></div></div>'
            '<div class="side-body" id="cartBody"></div>'
            '<div class="rail"><div class="hd">You might also like</div><div class="r">%s</div></div>'
            '<div class="osum" id="osum" style="display:none"><h4>Order Summary</h4>'
            '<div class="r"><span>Total MRP</span><b id="osMrp">₹0</b></div>'
            '<div class="r" id="osSaveRow"><span>Discount on MRP</span><b id="osSave" style="color:#0f7b47">₹0</b></div>'
            '<div class="r free"><span>Shipping</span><b>FREE</b></div>'
            '<div class="r tot"><span>Total Amount</span><b id="osTot">₹0</b></div></div>'
            '<div class="side-ft"><div class="ok">✓ Free 30-day returns on every order</div>'
            '<div class="coup"><input id="coupIn" placeholder="Coupon code"><button data-coupon>Apply</button></div>'
            '<button class="btn btn-d btn-blk" style="border-radius:5px" id="coBtn">Checkout</button>'
            '<div class="note">Secure payments · UPI, cards, netbanking &amp; free COD</div>'
            '</div></aside>' % (chips, rail))

def wish_drawer():
    return ('<aside class="side" id="wishDrw">'
            '<div class="side-hd"><button class="bk" data-close aria-label="Close">←</button>'
            '<h3>My Wishlist</h3><span style="width:20px"></span></div>'
            '<div class="wl-sel"><select><option>Main Wishlist</option><option>Festive picks</option>'
            '<option>Office edit</option></select><button title="New wishlist">+</button></div>'
            '<div class="side-body" id="wishBody"></div>'
            '<div class="side-ft"><div class="note" id="wlDrwCount" style="margin:0 0 9px"></div>'
            '<div class="two"><button class="btn btn-o" data-addall>Add all to cart</button>'
            '<button class="btn btn-d" data-close>Continue shopping</button></div></div></aside>')

def stories_modal():
    return ('<div class="stories" id="stories"><div class="st-card">'
            '<img id="stImg" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="">'
            '<div class="st-bars"></div>'
            '<div class="st-top"><span class="av">GC</span><span class="nm" id="stName"></span>'
            '<button class="x" data-close>×</button></div>'
            '<div class="st-nav"><div data-stprev></div><div data-stnext></div></div>'
            '<div class="st-cap" id="stCap"></div>'
            '<div class="st-ft"><img id="stFtImg" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="">'
            '<div><div class="n" id="stFtName"></div><div class="p" id="stFtPrice"></div></div>'
            '<button class="btn btn-p" id="stFtBtn" data-quick="">Add to bag</button></div>'
            '</div></div>')

def tabbar(active=''):
    items = [('home', 'home.html', IC['home'], ''),
             ('shop', 'collection.html', IC['menu'], ''),
             ('bag', '#', IC['bag'], ' data-opencart'),
             ('wish', '#', IC['heart'], ' data-openwish'),
             ('acct', '#', IC['user'], '')]
    out = []
    for key, href, icon, attr in items:
        cnt = ''
        if key == 'bag':
            cnt = '<i class="cnt" data-cartcount style="display:none">0</i>'
        if key == 'wish':
            cnt = '<i class="cnt" data-wishcount style="display:none">0</i>'
        out.append('<a href="%s"%s class="%s" aria-label="%s">%s%s</a>'
                   % (href, attr, 'on' if key == active else '', key, icon, cnt))
    return '<nav class="tabbar">%s</nav>' % ''.join(out)

SHOP_LINKS = ['Ankle Length Leggings', 'Joggers', 'Loungewear', 'Plus Size', 'Cargo Pants',
              'Kurti Pants', 'Active Wear', 'Blacks', 'Beige', 'Reds', 'Bell Bottoms',
              'Shimmer Leggings']

def footer():
    shop = ('<span class="sep">|</span>'.join(
        '<a href="collection.html">%s</a>' % E(s) for s in SHOP_LINKS))
    cols = ''.join(
        '<div><h4>%s</h4><ul>%s</ul></div>'
        % (E(k), ''.join('<li><a href="#">%s</a></li>' % E(x) for x in v))
        for k, v in FOOTER.items() if k != 'Shop')
    soc = ''.join('<a href="#" aria-label="%s">%s</a>' % (n, n[0]) for n in
                  ('Facebook', 'Instagram', 'YouTube', 'LinkedIn'))
    contact = ('<div><h4>Contact</h4>'
               '<div class="cx">%s<a href="#">customercare@gocolors.com</a></div>'
               '<div class="cx">%s<span>1800-123-9953 (10:00 AM–06:00 PM, Monday–Saturday)</span></div>'
               '<div class="cx">%s<span>7305959422</span></div>'
               '<div class="cx"><span style="font-size:11.5px;color:#777">CIN · L17291TN2010PLC077303</span></div>'
               '</div>' % (IC['mail'], IC['phone'], IC['wa']))
    policies = ''.join('<a href="#">%s</a>' % p for p in
                       ('Refund policy', 'Privacy policy', 'Terms of service', 'Shipping policy'))
    return ('<div class="shopbar"><div class="wrap"><h4>SHOP</h4><div class="lks">%s</div></div></div>'
            '<footer class="ftr"><div class="wrap"><div class="ftr-grid">'
            '<div>%s<div class="soc">%s</div></div>%s%s</div>'
            '<div class="bot"><div>%s</div>'
            '<span>© 2026, Go Colors India · interactive mockup, not the live store</span>'
            '</div></div></footer>'
            '<a class="appfab" href="#">Download The App</a>'
            % (shop, logo(), soc, cols, contact, policies))

def modal_shell():
    return ('<div class="ovl" id="ovl"></div>'
            '<div class="mod" id="quickMod"><div class="mod-box"></div></div>'
            '<div class="toast" id="toast"></div>')


def l1_bar(active=''):
    """The desktop L1 menu, carried into mobile as a sticky tab row."""
    links = ''.join('<a href="%s" class="%s">%s</a>'
                    % (href, 'on' if href == active else '', E(label))
                    for label, href in L1)
    return '<nav class="l1bar"><div class="in">%s</div></nav>' % links


def split_banner(key):
    tag, title, sub, c1, h1_, c2, h2_, disc, img = BANNERS[key]
    return ('<section class="sban">'
            '<div class="im"><img src="%s" alt="%s" fetchpriority="high"></div>'
            '<div class="bd">'
            '<span class="tag">%s %s</span>'
            '<h1>%s</h1>'
            '<div class="ctas">'
            '<a class="btn btn-d" href="%s">%s</a>'
            '<a class="btn btn-o" href="%s">%s</a>'
            '</div>'
            '</div></section>'
            % (U(img), E(title), IC['spark'], E(tag), E(title),
               h1_, E(c1), h2_, E(c2)))


STOP = set('and the for with your all new & pants pant wear'.split())


def _toks(s):
    out = []
    for w in re.findall(r'[a-z]+', s.lower()):
        if len(w) < 4 or w in STOP:
            continue
        out.append(w[:-1] if w.endswith('s') and len(w) > 4 else w)
    return out


def cat_start_price(audience, title):
    """Cheapest product in the audience whose type matches the category name."""
    pool = [p for p in PROD if p['whom'] == audience] or PROD
    want = _toks(title)
    if not want:
        want = [title.lower()[:5]]
    best = []
    for lvl in ('ty', 'both'):
        for p in pool:
            hay = ' '.join(_toks(p['ty'] if lvl == 'ty' else p['ty'] + ' ' + p['t']))
            if any(w in hay for w in want):
                best.append(p)
        if best:
            break
    return int(min(x['p'] for x in (best or pool)))


def category_card(title, img, sale, audience='Women'):
    tag = ''
    if sale:
        cls = 'sale new' if sale.strip().lower() in ('new in', 'new') else 'sale'
        tag = '<span class="%s">%s</span>' % (cls, E(sale))
    start = ('<span class="startsat">Starts at \u20b9%s</span>'
             % '{:,}'.format(cat_start_price(audience, title)))
    return ('<a class="cat" href="collection.html">'
            '<div class="ci">%s<img src="%s" alt="%s" loading="lazy">%s</div>'
            '<div class="n">%s<span class="ar">\u203a</span></div></a>'
            % (tag, U(img), E(title), start, E(title)))


def category_section(audiences, heading='Shop by category', sub=''):
    """Tabbed when several audiences are passed, a plain grid when one is."""
    head = ('<div class="sec-hd"><div><h2>%s</h2>%s</div>'
            '<a class="more" href="collection.html">View all</a></div>'
            % (E(heading), ('<div class="sub">%s</div>' % E(sub)) if sub else ''))
    def track(a):
        return ('<div class="catwrap">'
                '<button class="arw l" data-cats="p" aria-label="Previous categories">\u2039</button>'
                '<div class="cats">%s</div>'
                '<button class="arw r" data-cats="n" aria-label="More categories">\u203a</button>'
                '</div>' % ''.join(category_card(c[0], c[1], c[2], a) for c in CATEGORIES[a]))

    if len(audiences) == 1:
        return ('<section class="sec catsec"><div class="wrap">%s%s</div></section>'
                % (head, track(audiences[0])))
    tabrow = ''.join('<button data-tab="%s" class="%s">%s</button>'
                     % (a, 'on' if i == 0 else '', E(a)) for i, a in enumerate(audiences))
    panels = ''.join(
        '<div data-panel="%s" data-group="cats" style="%s">%s</div>'
        % (a, '' if i == 0 else 'display:none', track(a))
        for i, a in enumerate(audiences))
    return ('<section class="sec catsec"><div class="wrap">%s'
            '<div class="tabs" data-tabgroup="cats">%s</div>%s</div></section>'
            % (head, tabrow, panels))


RAIL_TABS = ['Bestsellers', 'New Arrivals', 'Trending Products']
RAIL_TAG = {'Bestsellers': 'Bestseller', 'New Arrivals': 'New in',
            'Trending Products': 'Trending'}


def _rail(items, gid, tab, show):
    return ('<div data-panel="%s" data-group="%s" style="%s">'
            '<div class="carou">'
            '<button class="arw l" data-rail="p" aria-label="Previous">\u2039</button>'
            '<div class="bsrail" data-cards>%s</div>'
            '<button class="arw r" data-rail="n" aria-label="Next">\u203a</button>'
            '</div></div>'
            % (tab, gid, '' if show else 'display:none',
               ''.join('<div data-p="%s" data-tag="%s"></div>' % (p['h'], E(RAIL_TAG[tab]))
                       for p in items)))


def product_tabs_section(audience, heading, sub='', gid='ptabs'):
    pools = POOLS[audience]
    head = ('<div class="sec-hd"><div><h2>%s</h2>%s</div>'
            '<a class="more" href="collection.html">View all</a></div>'
            % (E(heading), ('<div class="sub">%s</div>' % E(sub)) if sub else ''))
    tabs = ''.join('<button data-tab="%s" class="%s">%s</button>'
                   % (t, 'on' if i == 0 else '', E(t)) for i, t in enumerate(RAIL_TABS))
    rails = ''.join(_rail(pools[t], gid, t, i == 0) for i, t in enumerate(RAIL_TABS))
    return ('<section class="sec"><div class="wrap">%s'
            '<div class="pilltabs" data-tabgroup="%s">%s</div>%s</div></section>'
            % (head, gid, tabs, rails))

# --------------------------------------------------------------- page shell
def page(title, body, extra_js='', active='', pagekey='', l1=''):
    links = [('index.html', 'Overview'), ('home.html', 'Home'), ('women.html', 'Women'),
             ('men.html', 'Men'), ('girls.html', 'Girls'),
             ('collection.html', 'Collection'), ('product.html', 'Product'),
             ('wishlist.html', 'Wishlist')]
    nav = ''.join('<a href="%s" class="%s">%s</a>'
                  % (h, 'on' if h == pagekey else '', t) for h, t in links)
    bar = ('<div class="pbar"><span class="pb-logo">GO COLORS · MOCKUP</span>%s'
           '<span class="spacer"></span>'
           '<div class="tg"><button data-vp="d" class="on" onclick="setVp(\'d\')">Desktop</button>'
           '<button data-vp="m" onclick="setVp(\'m\')">Mobile</button></div></div>' % nav)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title>%s<style>%s</style></head>'
            '<body class="hasbar">%s<div id="viewport">%s%s%s%s%s</div>'
            '%s%s%s%s%s%s'
            '<script>var DATA=%s;var SHADELIST=%s;</script><script>%s</script>%s</body></html>'
            % (E(title), FONT_LINK, CSS, bar, app_strip(), header(), l1_bar(l1), body, footer(),
               tabbar(active), drawer(), search_overlay(), cart_drawer(), wish_drawer(),
               stories_modal() + modal_shell(),
               DATA_JSON, SHADE_JSON, JS, extra_js))

# --------------------------------------------------------------- home
def trust_bar():
    ics = [IC['truck'], IC['ret'], IC['cod']]
    lis = ''.join('<li>%s%s</li>' % (ics[i], E(t)) for i, t in enumerate(BRAND['trust'][:3]))
    return '<div class="trust"><ul>%s</ul></div>' % lis

def carousel(items, gid):
    return ('<div class="carou"><button class="arw l" data-rail="p" aria-label="Scroll left">\u2039</button>'
            '<div class="railrow" data-cards>%s</div>'
            '<button class="arw r" data-rail="n" aria-label="Scroll right">\u203a</button></div>'
            % cards_placeholder(items))


def shade_section(audience='All', gid='s1'):
    pool = POOLS[audience]['Bestsellers'][:8]
    return ('<section class="sec"><div class="wrap">'
            '<div class="sec-hd"><div><h2>Find Your Perfect Shade</h2>'
            '<div class="sub">Slide through the spectrum and shop the shade you love</div></div>'
            '<a class="more" href="collection.html">View all</a></div>'
            '%s'
            '<div class="spectrum"><input type="range" id="shadeRange" min="0" max="100" value="0" '
            'aria-label="Pick a shade">'
            '<div style="text-align:center"><span class="chip"><i id="shadeChipDot"></i>'
            '<span id="shadeChipName">Black</span></span></div></div>'
            '</div></section>' % carousel(pool, gid))


APP_PHONE = None  # set after PROD is built


def app_download():
    return ('<section class="appdl"><div class="wrap"><div class="ad-in">'
            '<div class="ph"><span class="notch"></span>'
            '<img src="%s" alt="Go Colors app" loading="lazy"></div>'
            '<div class="cp">'
            '<h2>More knockout offers waiting!</h2>'
            '<p>Extra 10%% off your first app order, early access to drops and '
            'one-tap reorders \u2014 only on the Go Colors app.</p>'
            '<div class="badges"><span class="dn">Download now</span>'
            '<a class="store" href="#"><span class="ic">%s</span>'
            '<span class="tx"><i>GET IT ON</i><b>Google Play</b></span></a>'
            '<a class="store" href="#"><span class="ic">%s</span>'
            '<span class="tx"><i>Download on the</i><b>App Store</b></span></a></div>'
            '</div></div></div></section>'
            % (PROD[0]['i'][0], IC['play'], IC['apple']))


def cards_placeholder(items):
    return ''.join('<div data-p="%s"></div>' % p['h'] for p in items)

def home():
    hero = split_banner('home')

    shop = category_section(['Women', 'Men', 'Girls'],
                            'Shop by category',
                            'Every collection across women, men and girls')

    bands = ''.join(
        '<a class="band" href="collection.html"><img src="%s" alt="%s" loading="lazy">'
        '<div class="lb">%s</div></a>' % (U(img), E(label), E(label))
        for label, img in PRICE_BANDS)
    price = '<section class="sec"><div class="wrap"><div class="bands">%s</div></div></section>' % bands

    stats = ''.join('<div><div class="n">%s</div><div class="l">%s</div></div>' % (E(a), E(b))
                    for a, b in BRAND['stats'])
    stat_sec = '<section class="sec grey" style="padding:0"><div class="wrap"><div class="stats">%s</div></div></section>' % stats

    best = product_tabs_section('All', 'Shop the edit',
                                'Bestsellers, new arrivals and what is trending right now')

    shade = shade_section('All', 's1')

    revs = ''.join(
        '<div class="rev"><div class="st">%s</div><p>“%s”</p>'
        '<div class="who">%s <span>· %s</span></div>'
        '<div class="vf">✓ Verified buyer · %s</div></div>'
        % ('★' * st + '☆' * (5 - st), E(txt), E(nm), E(city), E(prod))
        for nm, city, txt, st, prod in REVIEWS)
    rev_sec = ('<section class="sec grey"><div class="wrap">'
               '<h2 style="text-align:center;font-size:clamp(19px,2.3vw,26px)">Customers Reviews</h2>'
               '<div class="revsum" style="margin-top:10px"><span class="stars">★★★★☆</span>'
               '<b style="color:#1a1a1a">%s</b><span>· (%s)</span>'
               '<span class="vf">✓ Verified</span></div>'
               '<div class="revs">%s</div></div></section>'
               % (BRAND['rating'], BRAND['reviews'], revs))

    body = (hero + shop + best + price + stat_sec + rev_sec +
            shade + trust_bar() + app_download())
    return page("Shop Premium Women's Bottom Wear Online — Go Colors", body,
                active='home', pagekey='home.html', l1='home.html')


# --------------------------------------------------------------- audience landing
LANDING = {
 'women': ("Women's Bottomwear — Go Colors", 'Women', 'women.html'),
 'men':   ('Men — Go Colors',                'Men',   'men.html'),
 'girls': ('Girls — Go Colors',              'Girls', 'girls.html'),
}

def landing_page(key):
    title, audience, pagekey = LANDING[key]
    body = (split_banner(key)
            + category_section([audience], '%s categories' % audience,
                               'Shop the full %s range' % audience.lower())
            + product_tabs_section(audience, 'Shop the %s edit' % audience.lower(),
                                   'Bestsellers, new arrivals and trending styles',
                                   gid='ptabs-%s' % audience.lower())
            + shade_section(audience, 'sh-%s' % audience.lower())
            + trust_bar() + app_download())
    return page(title, body, active='home', pagekey=pagekey, l1=pagekey)

# --------------------------------------------------------------- collection
def filter_group(title, inner, open_=True):
    return ('<details class="fgrp"%s><summary>%s</summary>%s</details>'
            % (' open' if open_ else '', E(title), inner))

def chk(key, value, count, label=None):
    return ('<label class="fchk" data-f="%s|%s"><input type="checkbox">'
            '<span>%s</span><span class="ct">(%s)</span></label>'
            % (key, E(value), E(label or value), count))

def sidebar():
    whom = ''.join(chk('whom', k, v) for k, v in count_by('whom'))
    cols = ''.join('<i data-f="cl|%s" style="background:%s" title="%s"></i>'
                   % (E(c), COLOR_HEX.get(c, '#ccc'), E(c)) for c in ALL_COLOURS[:20])
    types = ''.join(chk('ty', k, v) for k, v in count_by('ty'))
    sizes = ''.join('<button class="fsz-b" data-f="sz|%s">%s</button>' % (s, s)
                    for s in ['XS', 'S', 'M', 'L', 'XL', '2X', '3X', '4X', '2P', '3P', '4P',
                              '26', '28', '30', '32', '34', '36', '38'])
    price = ('<div class="frange"><input type="range" id="priceRange" min="299" max="2299" '
             'step="50" value="2299" aria-label="Maximum price">'
             '<div class="lb"><span>₹299</span><span id="priceMax">₹2,299</span></div></div>')
    disc = chk('disc', '20', sum(1 for p in PROD if p['cp'] and (1 - p['p'] / p['cp']) >= .2),
               '20% & above')
    return ('<aside class="side-f"><h3>FILTERS</h3>'
            + filter_group('For Whom?', '<div class="bd">%s</div>' % whom)
            + filter_group('Colour', '<div class="fcols">%s</div>' % cols)
            + filter_group('Product Type', '<div class="bd">%s</div>' % types)
            + filter_group('Size', '<div class="fsz">%s</div>' % sizes)
            + filter_group('Price', price)
            + filter_group('Discount', '<div class="bd">%s</div>' % disc)
            + filter_group('Length', '<div class="bd">%s</div>'
                           % ''.join(chk('len', k, v) for k, v in count_by('len')), False)
            + filter_group('Fit', '<div class="bd">%s</div>'
                           % ''.join(chk('fit', k, v) for k, v in count_by('fit')), False)
            + filter_group('Pattern', '<div class="bd">%s</div>'
                           % ''.join(chk('pat', k, v) for k, v in count_by('pat')), False)
            + filter_group('Fabric', '<div class="bd">%s</div>'
                           % ''.join(chk('fab', k, v) for k, v in count_by('fab')), False)
            + filter_group('Rise', '<div class="bd">%s</div>'
                           % ''.join(chk('rise', k, v) for k, v in count_by('rise')), False)
            + '</aside>')

def collection():
    sort = ('<select class="sortsel" id="sortSel" aria-label="Sort by">'
            '<option value="rel">Sort By : Relevance</option>'
            '<option value="lh">Price: low to high</option>'
            '<option value="hl">Price: high to low</option>'
            '<option value="rt">Customer rating</option>'
            '<option value="dis">Biggest discount</option></select>')

    sheet = ('<div class="sheet" id="filterSheet"><div class="hd">'
             '<h3 style="font-size:14px">Filters</h3><button data-close>%s</button></div>'
             '<div class="bd">%s</div>'
             '<div class="ft"><button class="btn btn-o" data-clearf>Clear all</button>'
             '<button class="btn btn-d" data-close>Show results</button></div></div>'
             % (IC['x'], sidebar().replace('<aside class="side-f">', '<div>')
                                  .replace('</aside>', '</div>')
                                  .replace('<h3>FILTERS</h3>', '')))

    body = ('<div class="wrap"><div class="crumb"><a href="home.html">Home</a> / <b>New Arrivals</b></div>'
            '<div class="mfilter"><button data-filtersheet>%s Filter</button>'
            '<button data-sortsheet>⇅ Sort</button></div>'
            '<div class="plp">%s<div>'
            '<div class="plp-top"><span class="cnt" id="plpCount"></span>%s</div>'
            '<div class="chips" id="chips"></div>'
            '<div class="grid" id="plpGrid"></div>'
            '<div class="loadmore" id="loadWrap">'
            '<button class="btn btn-o" data-more>Load more &mdash; <span id="loadLeft"></span> left</button>'
            '</div></div></div></div>%s'
            % (IC['menu'], sidebar(), sort, sheet))
    return page("New Arrivals — Go Colors", body, '<script>%s</script>' % JS_PLP,
                active='shop', pagekey='collection.html', l1='')

# --------------------------------------------------------------- product
def product():
    p = BY['women-solid-black-cotton-mid-rise-kurti-pants']
    hero_colour = 'Black'
    gal_imgs = (p['i'] + [x[1] for x in PROD[6]['sw']] + p['i'])[:8]
    gallery = ('<div class="pgal" id="pgal">'
               '<span class="tg">Trending</span>'
               '<span class="tryon">%s Try It On</span>'
               '<button class="storyring" data-stories="%s" aria-label="Watch product stories">'
               '<span class="in">WATCH<br>THE FIT</span></button>%s</div>'
               % (IC['spark'], p['h'],
                  ''.join('<img src="%s" alt="%s" loading="%s">'
                          % (u, E(p['t']), 'eager' if i < 2 else 'lazy')
                          for i, u in enumerate(gal_imgs))))

    palette = ['Black', 'Baby Pink', 'Dark Purple', 'Teal', 'Dark Brown', 'Cherry', 'Fuchsia',
               'Brown', 'Wheat', 'Beige', 'Light Beige', 'Cream', 'Bottle Green', 'Dark Olive',
               'Navy', 'Maroon']
    dots = ''.join('<button data-pc="%s" class="%s" style="background:%s" title="%s"></button>'
                   % (E(c), 'on' if c == hero_colour else '', COLOR_HEX.get(c, '#ccc'), E(c))
                   for c in palette)
    sims = ''.join('<a href="product.html?p=%s"><img src="%s" alt="%s" loading="lazy">'
                   '<span>%s</span></a>' % (q['h'], q['i'][0], E(q['t']), E(lab))
                   for q, lab in [(BY['women-ikat-grey-mid-rise-printed-pencil-pant'], 'Ebony Grey'),
                                  (BY['women-solid-navy-cotton-mid-rise-kurti-pants'], 'Navy'),
                                  (BY['women-solid-wheat-cotton-mid-rise-kurti-pants'], 'Wheat')])
    sizes = ''.join('<button data-ps="%s"%s>%s</button>'
                    % (E(s), ' class="oos"' if i == len(p['sz']) - 1 else '', E(s))
                    for i, s in enumerate(p['sz']))
    disc = round((1 - p['p'] / p['cp']) * 100) if p['cp'] else 0

    usp3 = ''.join('<div>%s<span>%s</span></div>' % (ic, lab) for ic, lab in
                   [(IC['truck'], 'Free<br>Delivery'), (IC['ret'], 'Easy<br>Returns'),
                    (IC['cod'], 'Cash on<br>Delivery')])

    accordions = (
      '<div class="acc">'
      '<details open><summary>Product Details</summary><div class="ab">'
      'A mid-rise kurti pant cut in a cotton-rich stretch knit that holds its shape through the day. '
      'The elasticated waistband sits flat under kurtas, side pockets are deep enough for a phone, '
      'and the straight leg finishes at the ankle.'
      '<ul><li>Elasticated comfort waistband, no drawcord bulk</li>'
      '<li>Two side pockets</li><li>Straight leg, ankle length</li>'
      '<li>Available XS–4X plus petite-plus 2P–4P</li></ul></div></details>'
      '<details><summary>Specifications</summary><div class="ab dl">%s</div></details>'
      '<details><summary>Washing Instructions</summary><div class="ab">'
      'Machine wash cold with like colours. Do not bleach. Tumble dry low or line dry in shade. '
      'Warm iron if needed. Do not dry clean.</div></details>'
      '<details><summary>Reviews</summary><div class="ab">'
      '<b>%.1f out of 5</b> · %s reviews · 92%% say the fit is true to size.'
      '<p style="margin:12px 0 0">“%s” — %s, %s</p></div></details>'
      '</div>' % (
        ''.join('<div><span>%s</span><span>%s</span></div>' % (k, v) for k, v in [
            ('Fabric', 'Cotton stretch'), ('Fit', 'Regular fit'), ('Rise', 'Mid rise'),
            ('Closure', 'Elasticated waistband'), ('Pockets', '2 side pockets'),
            ('Length', 'Ankle length'), ('Pattern', 'Solid'), ('Country of origin', 'India'),
            ('Sizes', 'XS – 4X, 2P – 4P'), ('SKU', 'LPT1')]),
        p['r'], p['rc'], REVIEWS[1][2], REVIEWS[1][0], REVIEWS[1][1]))

    info = ('<div class="pdp-info">'
            '<h1>%s</h1>'
            '<div class="sku">%s : LPT1 | %s</div>'
            '<div class="pdp-rt"><span class="stars">%s</span><b style="color:#1a1a1a">%.1f</b>'
            '<span>| (%s)</span></div>'
            '<div class="pdp-mrp">MRP: <b>₹ %s</b>%s</div>'
            '<div class="pdp-tax">(Inclusive of all taxes)</div>'
            '<div class="rew"><div class="t"><i>GO</i> You\'re one tap away</div>'
            '<div class="b"><p>Join Go Rewards to reveal the coupons available on this order.</p>'
            '<button class="jb" data-coupon>Join Go Rewards</button>'
            '<p class="fine">Members save an average of <b>₹250</b> per order.</p></div></div>'
            '<div class="pbox"><div class="h"><span>Select Colour — '
            '<b id="pcName">%s</b></span><span class="nav2">‹ ›</span></div>'
            '<div class="cdots">%s</div>'
            '<div class="simw"><div class="h">3 similar styles</div><div class="simc">%s</div></div></div>'
            '<div class="pbox"><div class="h"><span>Select Size</span>'
            '<a href="#" data-sizeguide>Size guide ›</a></div>'
            '<div class="szrow">%s</div>'
            '<div class="err" id="pErr">Please pick a size to add this to your bag</div></div>'
            '<div class="pinbox"><div class="h">Check Serviceability</div>'
            '<div class="pin"><input id="pinIn" placeholder="Enter pincode" maxlength="6">'
            '<button data-pin>Check</button></div>'
            '<div class="pinres" id="pinRes"></div></div>'
            '<div id="atcAnchor"></div>'
            '<div class="atc"><span class="qty"><button data-pq="-1">−</button>'
            '<span id="pQty">1</span><button data-pq="1">+</button></span>'
            '<button class="btn btn-d" id="pdpAdd">%s Add to bag</button>'
            '<button class="wbtn" data-wtog="%s" aria-label="Save to wishlist">%s</button></div>'
            '<div class="usp3">%s</div>%s</div>'
            % (E(p['t']), E(p['ty']), hero_colour,
               '★' * round(p['r']) + '☆' * (5 - round(p['r'])), p['r'], p['rc'],
               '{:,}'.format(int(p['p'])),
               ('<s>₹ %s</s><em>%d%% Off</em>' % ('{:,}'.format(int(p['cp'])), disc)) if p['cp'] else '',
               hero_colour, dots, sims, sizes, IC['bag'], p['h'], IC['heart'], usp3, accordions))

    secs = [('overview', 'Overview'), ('details', 'Details'), ('faqs', 'FAQs'),
            ('reviews', 'Reviews'), ('similar', 'You may like')]
    subnav = ('<div class="subnav" id="subnav"><div class="in">%s</div></div>'
              % ''.join('<button data-go="%s">%s</button>' % (i, E(l)) for i, l in secs))

    overview = ('<section class="pdp-sec" id="overview"><h2>Why women reorder this fit</h2>'
                '<p style="font-size:13.5px;line-height:1.85;color:#444;max-width:860px">'
                'The kurti pant is the piece our customers replace rather than replace with something '
                'else. It is cut for Indian body types, tested across the full size run, and made in a '
                'cotton stretch that keeps its shape after thirty washes. If you wear kurtas daily, '
                'this is the pant that disappears under them — no bunching at the ankle, no waistband '
                'digging in by evening.</p></section>')

    details = ('<section class="pdp-sec" id="details"><h2>Fit &amp; fabric</h2>'
               '<div class="acc dl" style="max-width:760px;border:0">%s</div></section>'
               % ''.join('<div><span>%s</span><span>%s</span></div>' % (k, v) for k, v in [
                   ('Model height', '5\'7", wearing size S'), ('Stretch', '4-way, 12% elastane'),
                   ('Waist (size M)', '30–32 inches'), ('Inseam', '38 inches'),
                   ('Transparency', 'Opaque'), ('Season', 'All season')]))

    faqs = ('<section class="pdp-sec" id="faqs"><h2>Frequently asked</h2><div class="acc">%s</div></section>'
            % ''.join('<details%s><summary>%s</summary><div class="ab">%s</div></details>'
                      % (' open' if i == 0 else '', E(q), E(a)) for i, (q, a) in enumerate(FAQ)))

    revs = ''.join(
        '<div class="rev"><div class="st">%s</div><p>“%s”</p>'
        '<div class="who">%s <span>· %s</span></div><div class="vf">✓ Verified buyer</div></div>'
        % ('★' * st + '☆' * (5 - st), E(txt), E(nm), E(city))
        for nm, city, txt, st, _pr in REVIEWS[:3])
    reviews = ('<section class="pdp-sec" id="reviews"><h2>Customer reviews</h2>'
               '<div class="revsum" style="justify-content:flex-start">'
               '<b style="color:#1a1a1a;font-size:28px">%.1f</b><span class="stars">★★★★☆</span>'
               '<span>%s reviews · 92%% say the fit is true to size</span></div>'
               '<div class="revs">%s</div></section>' % (p['r'], p['rc'], revs))

    similar = ('<section class="pdp-sec" id="similar"><h2>Mostlysane Collection</h2>'
               '<div class="carou"><button class="arw l" data-rail="p">‹</button>'
               '<div class="railrow" data-cards>%s</div>'
               '<button class="arw r" data-rail="n">›</button></div></section>'
               % cards_placeholder(PROD[12:20]))

    satc = ('<div class="satc" id="satc"><div class="in">'
            '<img id="satcImg" src="%s" alt="">'
            '<div><div class="n">%s</div><div class="r">★ %.1f (%s) · Free returns</div></div>'
            '<div class="p">₹ %s</div>'
            '<button class="btn btn-d" data-quick="%s">Add to bag</button></div></div>'
            % (p['i'][0], E(p['t']), p['r'], p['rc'], '{:,}'.format(int(p['p'])), p['h']))

    body = ('<div class="wrap"><div class="crumb"><a href="home.html">Home</a> / '
            '<a href="collection.html">Women</a> / <a href="collection.html">Kurti Pants</a> / <b>%s</b></div>'
            '<div class="pdp">%s%s</div></div>%s'
            '<div class="wrap">%s%s%s%s%s</div>%s'
            % (E(p['t']), gallery, info, subnav,
               overview, details, faqs, reviews, similar, satc))

    js = '<script>var HANDLE="%s";</script><script>%s</script>' % (p['h'], JS_PDP)
    return page('%s — Go Colors' % p['t'], body, js, active='shop', pagekey='product.html', l1='')

# --------------------------------------------------------------- wishlist page
def wishlist():
    body = ('<div class="wrap"><div class="crumb"><a href="home.html">Home</a> / <b>Wishlist</b></div>'
            '<div style="padding:6px 0 18px"><h1 style="font-size:clamp(20px,2.4vw,28px)">My Wishlist</h1>'
            '<div class="plp-top"><span class="cnt" id="wlCount"></span>'
            '<button class="btn btn-d" style="border-radius:5px;padding:11px 20px" data-addall>Add all to cart</button>'
            '</div></div>'
            '<div class="grid" id="wlGrid"></div>'
            '<div class="wl-empty" id="wlEmpty" style="display:none">'
            '<h2>Nothing saved yet</h2>'
            '<p>Tap the heart on any style and it will wait for you here.</p>'
            '<a class="btn btn-d" href="collection.html">Browse bottomwear</a></div></div>')
    return page('Wishlist — Go Colors', body, '<script>%s</script>' % JS_WISH,
                active='wish', pagekey='wishlist.html', l1='')

def cart_redirect():
    return ('<!doctype html><html><head><meta charset="utf-8"><title>Bag — Go Colors</title>'
            '<meta http-equiv="refresh" content="0;url=home.html"></head>'
            '<body><script>location.replace("home.html")</script>'
            '<p style="font-family:system-ui;padding:30px">The bag opens as a drawer. '
            '<a href="home.html">Return to the store</a>.</p></body></html>')

# --------------------------------------------------------------- hub
def index():
    pages = [
        ('home.html', 'Home', 'Hero, category tabs, budget edits, coverflow campaign slider, '
                              'best-seller carousels, shade finder, stats and the full footer.'),
        ('collection.html', 'Collection / PLP', 'Left-rail filters with live counts, price slider, '
                                                'sort, active-filter chips, quick-view and colour dots.'),
        ('product.html', 'Product / PDP', 'Two-up image grid, Go Rewards panel, colour dots and similar '
                                          'styles, size chips, pincode check, sticky add-to-bag, '
                                          'product stories, sticky section nav.'),
        ('wishlist.html', 'Wishlist', 'Saved styles as a page; the header heart opens the drawer version.'),
    ]
    cards = ''.join('<a href="%s"><div class="n">%s</div><div class="d">%s</div></a>'
                    % (h, E(n), E(d)) for h, n, d in pages)
    body = ('<div class="hub"><h1>Go Colors — interactive mockup</h1>'
            '<p class="lead">A replica of gocolors.com with the conversion improvements applied: '
            'a quick-view variant modal on every surface, a free-shipping progress bar and coupon '
            'field directly above a value-bearing checkout button, sticky add-to-bag on the product '
            'page, size guidance at the point of choice, and trust messaging beside every decision. '
            'Use the Desktop / Mobile toggle in the top bar to switch viewports.</p>'
            '<div class="hublist">%s</div>'
            '<div class="note"><b>How to use this.</b> Images load straight from the Go Colors '
            'Shopify CDN, so keep a network connection open. The bag and wishlist persist in your '
            'browser, so clearing site data resets them. Product names, images, colours and prices '
            'are the live catalogue as captured on 4 September 2026; reviews, ratings and stock '
            'nudges are sample content for demonstration and are not real customer data.</div></div>'
            % cards)
    return page('Go Colors mockup — overview', body, pagekey='index.html')


# --------------------------------------------------------------- optional localiser
IMG_RE = re.compile(r'https?://[^\s"\')]+?\.(?:jpg|jpeg|png|webp)(?:\?[^\s"\')]*)?', re.I)

def localise(files):
    """--local: download every CDN image into assets/ for offline use / QA."""
    import requests
    assets = os.path.join(OUT, 'assets')
    os.makedirs(assets, exist_ok=True)
    urls, texts = set(), {}
    for f in files:
        t = open(f, encoding='utf-8').read()
        texts[f] = t
        urls.update(IMG_RE.findall(t))
    print('  localising %d images...' % len(urls))

    def grab(u):
        ext = re.sub(r'\?.*$', '', u).rsplit('.', 1)[-1].lower()
        name = hashlib.md5(u.encode()).hexdigest() + '.' + ext
        path = os.path.join(assets, name)
        if not os.path.exists(path):
            for _ in range(3):
                try:
                    r = requests.get(u, timeout=60, headers={'User-Agent': 'Mozilla/5.0'})
                    r.raise_for_status()
                    open(path, 'wb').write(r.content)
                    break
                except Exception:
                    continue
            else:
                return u, None
        return u, 'assets/' + name

    mapping = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for u, rel in ex.map(grab, sorted(urls)):
            if rel:
                mapping[u] = rel
    for f, t in texts.items():
        for u, rel in mapping.items():
            t = t.replace(u, rel)
        open(f, 'w', encoding='utf-8').write(t)
    print('  localised %d/%d' % (len(mapping), len(urls)))

# --------------------------------------------------------------- main
def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    pages = {
        'index.html': index(), 'home.html': home(),
        'women.html': landing_page('women'), 'men.html': landing_page('men'),
        'girls.html': landing_page('girls'),
        'collection.html': collection(),
        'product.html': product(), 'wishlist.html': wishlist(), 'cart.html': cart_redirect(),
    }
    for name, htm in pages.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(htm)
        print('  wrote %-16s %5.0f KB' % (name, len(htm) / 1024))
    if '--local' in sys.argv:
        localise([os.path.join(OUT, n) for n in pages if n != 'cart.html'])
    print('done →', OUT)

if __name__ == '__main__':
    main()
