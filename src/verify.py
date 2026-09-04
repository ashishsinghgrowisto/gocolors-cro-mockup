import os, json
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gocolors-mockups')
SHOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots')
os.makedirs(SHOT, exist_ok=True)
PAGES = ['index', 'home', 'collection', 'product', 'wishlist']
report = {}

with sync_playwright() as pw:
    b = pw.chromium.launch()
    for vname, w, h in [('desktop', 1440, 950), ('mobile', 414, 860)]:
        ctx = b.new_context(viewport={'width': w, 'height': h})
        pg = ctx.new_page()
        errs = []
        pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errs.append('PAGEERROR: %s' % e))
        for name in PAGES:
            errs.clear()
            pg.goto('file://%s/%s.html' % (OUT, name))
            pg.wait_for_timeout(2600)
            pg.mouse.wheel(0, 2600); pg.wait_for_timeout(1400)
            pg.mouse.wheel(0, 3000); pg.wait_for_timeout(1400)
            pg.mouse.wheel(0, -9000); pg.wait_for_timeout(700)
            broken = pg.evaluate("""() => Array.from(document.images)
                .filter(i=>i.complete && i.naturalWidth===0)
                .map(i=>(i.getAttribute('src')||'(empty)').slice(0,80)).slice(0,6)""")
            pg.screenshot(path='%s/%s-%s.png' % (SHOT, name, vname),
                          full_page=(name in ('index',)))
            report['%s-%s' % (name, vname)] = {'errors': errs[:5], 'broken': broken}
        ctx.close()

    ctx = b.new_context(viewport={'width': 1440, 'height': 950})
    pg = ctx.new_page()
    ierr = []
    pg.on('pageerror', lambda e: ierr.append(str(e)))
    pg.on('console', lambda m: ierr.append(m.text) if m.type == 'error' else None)

    pg.goto('file://%s/home.html' % OUT); pg.wait_for_timeout(2600)
    pg.hover('.nav > li:first-child .top'); pg.wait_for_timeout(700)
    mega = pg.evaluate("""() => getComputedStyle(document.querySelector('.nav>li .mega')).visibility
        + ' links:' + document.querySelectorAll('.nav>li:first-child .mega a.mlink').length""")
    pg.screenshot(path=SHOT + '/i-mega.png')
    pg.mouse.move(700, 700); pg.wait_for_timeout(300)

    pg.click('[data-search]'); pg.wait_for_timeout(900)
    pg.screenshot(path=SHOT + '/i-search.png')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(500)

    covermid = pg.evaluate("() => {var m=document.querySelector('.cover-tr>a.mid');return m?m.innerText.slice(0,24):null}")
    shade = pg.evaluate("""() => {var r=document.querySelector('#shadeRange');
        r.value=55;r.dispatchEvent(new Event('input'));
        return document.querySelector('#shadeChipName').textContent}""")

    pg.click('.card .atcbtn'); pg.wait_for_timeout(900)
    pg.screenshot(path=SHOT + '/i-quick.png')
    pg.click('#qSz button:nth-child(2)'); pg.wait_for_timeout(250)
    pg.click('[data-qadd]'); pg.wait_for_timeout(1400)
    pg.screenshot(path=SHOT + '/i-cart.png')
    cart = pg.evaluate("""() => ({n:document.querySelector('[data-cartcount]').textContent,
        co:document.querySelector('#coBtn').textContent,
        mrp:document.querySelector('#osMrp').textContent,
        tot:document.querySelector('#osTot').textContent})""")
    pg.keyboard.press('Escape'); pg.wait_for_timeout(400)
    pg.click('.card .wishbtn'); pg.wait_for_timeout(500)
    pg.click('[data-openwish]'); pg.wait_for_timeout(900)
    pg.screenshot(path=SHOT + '/i-wishdrawer.png')
    wdraw = pg.evaluate("() => document.querySelectorAll('#wishBody .ci').length")
    pg.keyboard.press('Escape'); pg.wait_for_timeout(400)

    pg.goto('file://%s/collection.html' % OUT); pg.wait_for_timeout(2200)
    n0 = pg.evaluate("() => document.querySelectorAll('#plpGrid .card').length")
    pg.click('.side-f [data-f="ty|Kurti Pants"]'); pg.wait_for_timeout(700)
    n1 = pg.evaluate("() => document.querySelectorAll('#plpGrid .card').length")
    chips = pg.evaluate("() => document.querySelector('#chips').textContent.trim()")
    pg.screenshot(path=SHOT + '/i-filter.png')
    pg.click('[data-clearf]'); pg.wait_for_timeout(500)
    prange = pg.evaluate("""() => {var r=document.querySelector('#priceRange');
        r.value=599;r.dispatchEvent(new Event('input'));
        return document.querySelectorAll('#plpGrid .card').length}""")
    pg.wait_for_timeout(400)
    pg.click('[data-clearf]'); pg.wait_for_timeout(400)
    pg.select_option('#sortSel', 'lh'); pg.wait_for_timeout(600)
    first = pg.evaluate("() => document.querySelector('#plpGrid .pr b').textContent")

    pg.goto('file://%s/product.html' % OUT); pg.wait_for_timeout(2600)
    pg.click('.cdots button:nth-child(3)'); pg.wait_for_timeout(400)
    colour = pg.evaluate("() => document.querySelector('#pcName').textContent")
    pg.fill('#pinIn', '482001'); pg.click('[data-pin]'); pg.wait_for_timeout(500)
    pin = pg.evaluate("() => document.querySelector('#pinRes').classList.contains('on')")
    pg.screenshot(path=SHOT + '/i-pdp.png')
    pg.click('.storyring'); pg.wait_for_timeout(1200)
    pg.screenshot(path=SHOT + '/i-stories.png')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(400)
    pg.mouse.wheel(0, 1900); pg.wait_for_timeout(900)
    satc = pg.evaluate("() => document.querySelector('#satc').classList.contains('on')")
    subnav = pg.evaluate("() => document.querySelector('#subnav').classList.contains('show')")
    pg.screenshot(path=SHOT + '/i-pdp-sticky.png')

    ctx2 = b.new_context(viewport={'width': 414, 'height': 860}, is_mobile=True, has_touch=True)
    p2 = ctx2.new_page()
    p2.goto('file://%s/home.html' % OUT); p2.wait_for_timeout(2200)
    p2.click('[data-burger]'); p2.wait_for_timeout(600)
    p2.click('[data-mtab="Men"]'); p2.wait_for_timeout(700)
    p2.screenshot(path=SHOT + '/i-drawer-sub.png')
    drilled = p2.evaluate("""() => document.querySelector('[data-mpanel="Men"]').style.display !== 'none'
        && document.querySelector('[data-mpanel="Women"]').style.display === 'none'""")
    p2.click('[data-mtab="Girls"]'); p2.wait_for_timeout(500)
    backok = p2.evaluate("""() => document.querySelectorAll('[data-mpanel="Girls"] .dgrid a').length > 5""")
    p2.keyboard.press('Escape'); p2.wait_for_timeout(400)
    p2.goto('file://%s/collection.html' % OUT); p2.wait_for_timeout(2000)
    p2.click('[data-filtersheet]'); p2.wait_for_timeout(700)
    p2.screenshot(path=SHOT + '/i-sheet.png')
    sheet = p2.evaluate("() => document.querySelector('#filterSheet').classList.contains('on')")
    b.close()

report['interactions'] = dict(mega=mega, coverMid=covermid, shadeChip=shade, cart=cart,
                              wishDrawerItems=wdraw, plpAll=n0, plpFiltered=n1, chips=chips,
                              priceFiltered=prange, sortFirst=first, pdpColour=colour,
                              pinOk=pin, stickyATC=satc, subnav=subnav,
                              drawerDrill=drilled, drawerBack=backok, filterSheet=sheet,
                              errors=ierr[:8])
print(json.dumps(report, indent=1, ensure_ascii=False))
