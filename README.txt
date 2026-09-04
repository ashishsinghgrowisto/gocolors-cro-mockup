GO COLORS — INTERACTIVE MOCKUP (CRO-improved variant)
=====================================================

Open index.html in any browser. Images load straight from the Go Colors
Shopify CDN, so keep a network connection open.

PAGES
  index.html        Overview / hub
  home.html         Homepage
  collection.html   Collection (PLP)
  product.html      Product detail (PDP)
  wishlist.html     Saved styles
  cart.html         Redirects to home — the bag opens as a drawer

CONTROLS
  Top black bar     Page links + a Desktop / Mobile viewport toggle
  Bag & wishlist    Persist in the browser (localStorage); clearing site
                    data resets them

MATCHED TO THE LIVE SITE
  App-download strip and green rule above the header; logo, Women / Men
  (NEW) / Girls nav with full-width mega menus; centred search; Stores,
  Account, Wishlist and Bag icons with labels and live counts; mobile
  hamburger drawer with drill-down and an icon-only bottom tab bar.
  Home: full campaign banner, Bottoms / Tops / Men category tabs, 3-item
  trust bar, budget tiles with the label below the image, coverflow
  campaign slider with arrows and dots, left-aligned stats band, pill
  tabs (Best Sellers / Trending Now / Steal Deals) over product
  carousels, Find Your Perfect Shade with the colour spectrum slider,
  honest-pricing block, reviews, black SHOP link bar, white four-column
  footer and the floating Download The App pill.
  PLP: left filter rail with live counts, colour swatch grid, size chips,
  price slider, sort dropdown at right, 4-column grid with quick-view eye.
  PDP: two-up image grid, "Kurti Pants : LPT1 | Black" SKU line, Go
  Rewards panel, colour dots with similar styles, round size chips,
  Check Serviceability, quantity stepper beside a black ADD TO BAG, and
  Product Details / Specifications / Washing Instructions / Reviews
  accordions.
  Bag: Cart — Checkout — Payment stepper, three trust chips, per-line
  size dropdown and quantity, "30 days return available", recommendation
  rail and an order summary.
  Wishlist: slide-in drawer with the wishlist selector, plus a full page.
  Search: Categories / Trending searches / Top products.

CRO CHANGES APPLIED (this is not a pixel-for-pixel copy)
  · Quick-view variant modal from every surface — cards, cart rail,
    stories and the sticky bar — one consistent component
  · Free-shipping progress bar at the top of the bag
  · Coupon field directly above the checkout button, with the order value
    carried on the button itself ("Checkout @ ₹X")
  · Sticky add-to-bag bar on the PDP with image, rating and price
  · Inline "please pick a size" error instead of a silent dead button
  · Size guide linked at the point of size selection
  · Trust row repeated beside every add-to-bag
  · Colour dots on cards that swap the card image
  · Sticky PDP section nav with scrollspy; product stories reel
  · Active-filter chips and load-more on the PLP

NOTE ON CONTENT
  Reviews, ratings, stock nudges and the Go Rewards saving figure are
  sample content for demonstration. They are not real Go Colors customer
  data and should be replaced before any external use.

REBUILDING
  Sources are in src/ (build_mockups.py with data.py, style.py, script.py).
    python3 build_mockups.py            → CDN image URLs (this build)
    python3 build_mockups.py --local    → downloads every image into
                                          assets/ for fully offline use
