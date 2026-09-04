# -*- coding: utf-8 -*-
"""Captured Go Colors data (live site, gocolors.com)."""

P  = 'https://cdn.shopify.com/s/files/1/0598/8158/6848/'
P2 = 'https://gocolors.com/cdn/shop/files/'

def U(s):
    if not s: return ''
    if s.startswith('~'): return P + s[1:]
    if s.startswith('^'): return P2 + s[1:]
    return s

BRAND = dict(
    name='Go Colors',
    tagline='Life moves in your comfort zone',
    hero='^Website_Banner_-_SK-KV2_600_x_800.jpg',
    heroKicker='LIFE MOVES IN YOUR',
    heroTitle='COMFORT ZONE',
    heroCta='Explore Now',
    stats=[('8 Million+','Happy Customers'),('1200+','Bottomwear Styles'),
           ('120+','Colors & Prints'),('750+','Exclusive Stores')],
    trust=['Free Shipping','30-Day Easy Returns','Free COD','Secure Payments'],
    rating='4.37', reviews='1,772',
)

ANNOUNCE = ['FREE SHIPPING ON EVERY ORDER', '30-DAY EASY RETURNS',
            'FREE CASH ON DELIVERY', '8 MILLION+ HAPPY CUSTOMERS',
            'EXTRA 10% OFF ON PREPAID']

# ---- navigation -------------------------------------------------------------
NAV = [
 ('Women', '#', [
   ('New Arrivals','^women-new-arrivals-nav.jpg','New in this week'),
   ('Best Sellers','^women-best-sellers-nav.jpg','Most loved styles'),
   ('Leggings & Churidar','^women-leggings-churidar-nav.jpg','Ankle, full & churidar'),
   ('Kurti Pants','^women-kurti-pants-nav.jpg','Everyday ethnic fits'),
   ('Wide Pants','^women-wide-pants-nav.jpg','Palazzos & parachute'),
   ('Straight & Tapered','^women-straight-tapered-pants-nav.jpg','Office-ready pants'),
   ('Jeggings','^women-jeggings-nav.jpg','Super stretch denim'),
   ('Active & Athleisure','^women-active-athleisure-nav.jpg','Train, walk, lounge'),
   ('Shorts & Capris','^women-shorts-capris-nav.jpg','Warm-weather picks'),
   ('Jeans & Denims','^women-jeans-denims-nav.jpg','Skinny to culottes'),
   ('Ethnic','^women-ethnic-nav.jpg','Salwars & harems'),
   ('Dresses','^women-dresses-nav.jpg','Short, midi & long'),
 ]),
 ('Men', '#', [
   ('Pants & Trousers','^men-pants-trousers-nav.jpg','Everyday tailoring'),
   ('Cargos','^men-cargos-nav.jpg','Utility pockets'),
   ('Chinos','^men-chinos-nav.jpg','Smart casual'),
   ('Jeans & Denims','^men-jeans-denims-nav.jpg','Stretch denim'),
   ('Shorts','^men-shorts-nav.jpg','Off-duty fits'),
 ]),
 ('Girls', '#', [
   ('Leggings','^women-leggings-churidar-nav.jpg','School to play'),
   ('Jeggings','^women-jeggings-nav.jpg','Denim look, knit feel'),
   ('Pants','^women-kurti-pants-nav.jpg','All-day comfort'),
   ('Shorts','^women-shorts-capris-nav.jpg','Summer ready'),
 ]),
]


# ---- grouped mega-menu hierarchy (Myntra-style columns) ---------------------
NAV_GROUPS = {
 'Women': [
   ('Bottomwear', ['Leggings & Churidar', 'Ankle Length Leggings', 'Kurti Pants',
                   'Wide Pants', 'Palazzos', 'Straight & Tapered Pants',
                   'Pleated Pants', 'Cargos']),
   ('Denims & Jeggings', ['Jeggings', 'Super Stretch Jeggings', 'Printed Jeggings',
                          'Denim Leggings', 'Jeans & Denims', 'Denim Culottes',
                          'Skinny Jeans']),
   ('Ethnic & Festive', ['Ethnic', 'Salwars', 'Churidars', 'Harem Pants',
                         'Kurti / Kurta', 'Skirts & Skorts']),
   ('Active & Athleisure', ['Joggers', 'Track Pants', 'Yoga Leggings',
                            'Shorts & Capris', 'Cycling Shorts', 'Training Capri']),
   ('Tops & Dresses', ['T-Shirts & Knit Tops', 'Printed Shirts', 'Solid Shirts',
                       'Blouses', 'Short Dress', 'Midi Dress']),
   ('Shop By Edit', ['New Arrivals', 'Best Sellers', 'Shimmer Leggings',
                     'Plus Size', 'Office Wear', 'Under \u20b9599']),
 ],
 'Men': [
   ('Pants & Trousers', ['Pants & Trousers', 'Chinos', 'Flex Knit Pants',
                         'Glide Tech Trousers', 'Utility Pants', 'Pull-On Pants']),
   ('Jeans & Cargos', ['Jeans & Denims', 'Slim Fit Denims', 'Regular Fit Denims',
                       'Cargos', 'Cargo Sweatpants', 'Denim Joggers']),
   ('Topwear', ['Shirts', 'Casual Cotton Shirt', 'Premium Cotton Shirt',
                'Polos', 'Classic Pique Polo', 'T-Shirts']),
   ('Active & Lounge', ['Track Pant', 'Casual Joggers', 'Active Shorts',
                        'EaseFlex Lounge Pants', 'EaseFlex Lounge Shorts']),
   ('Shorts', ['Shorts', 'Casual Shorts', 'Urban Cargo Shorts']),
   ('Shop By Edit', ['New Arrivals', 'Best Sellers', 'Office Wear', 'Weekend Edit']),
 ],
 'Girls': [
   ('Leggings', ['Leggings', 'Cropped Leggings', 'Girls 3/4th Leggings']),
   ('Jeggings & Pants', ['Denim Jeggings', 'Super Stretch Jeggings',
                         'Knit Jeggings', 'Pants', 'Harem Pants']),
   ('Shorts', ['Knit Shorts', 'Cycling Shorts']),
   ('Shop By Edit', ['New Arrivals', 'Best Sellers', 'School Edit', 'Playtime']),
 ],
}

MEGA_PROMOS = [
  ('^Inside_banners_230x100-06.jpg','Wide Pants'),
  ('^Inside_banners_230x100-09.jpg','MostlySane Edit'),
  ('^Inside_banners_230x100-10.jpg','Formal Wear'),
  ('^Inside_banners_230x100-07.jpg','Wanderlust'),
]

SIZES_CHIPS = ['XS','S','M','L','XL','2X','3X','4X','Plus 2P–4P']

# ---- home page sections -----------------------------------------------------
CAT_TABS = {
 'Bottoms': [
   ('Ankle Length Leggings','^Ankle_length_churidar_550x550.jpg'),
   ('Palazzos','^Hakoba_Palazzo_550x550.jpg'),
   ('Wide Pants','^Parachute_pant_02_550x550.jpg'),
   ('Kurti Pants','^Kurti_pant_550x550.jpg'),
   ('Skirts & Skorts','^Twill_skort_e5c57bef-0f59-4bb4-8abb-3a897654fb2c_550x550.jpg'),
   ('Joggers','^Casula_jogger_550x550.jpg'),
   ('Cargos','^Cargo_sweatpant_550x550.jpg'),
   ('Jeggings','^Denim_jegging_550x550.jpg'),
   ('Ethnics','^Harem_pant_02_550x550.jpg'),
 ],
 'Tops': [
   ('Printed Shirts','^Resizes_Printedshirts_550x550.jpg'),
   ('Solid Shirts','^Resizes_SolidShirts_550x550.jpg'),
   ('Short Dress','^Resizes_Shortdress_550x550.jpg'),
   ('Midi Dress','^Resizes_MIDIdress_550x550.jpg'),
   ('Long Dress','~files/GoColors-ECommerceMay_248467.jpg'),
   ('T-Shirts & Knit Tops','^Resizes_Tshirt_550x550.jpg'),
   ('Blouses','^Resizes_Blouse_550x550.jpg'),
   ('Kurti / Kurta','^Resizes_Kurta_550x550.jpg'),
 ],
 'Men': [
   ('Pants & Trousers','~files/2_42ac893b-fe1a-4f5c-87d1-2e0221e73aa6.jpg'),
   ('Chinos','^Resizes_Chinoscopy_550x550.jpg'),
   ('Shirts','^Resizes_Shirtscopy_550x550.jpg'),
   ('Jeans & Denims','^Resizes_Jeanscopy_550x550.jpg'),
   ('Cargos','^Resizes_Cargopantscopy_550x550.jpg'),
   ('Polos','^Resizes_Poloscopy_550x550.jpg'),
   ('Shorts','^Resizes_Shortscopy_550x550.jpg'),
   ('T-Shirts','^Resizes_Tshirtcopy_550x550.jpg'),
 ],
}

PRICE_BANDS = [
  ('Under ₹399','^freepik__generate-a-premium-ultrarealistic-lifestyle-fashio__43135.png'),
  ('Under ₹599','^magnific_generate-a-premium-ultrar_2999765226.jpg'),
  ('Under ₹999','^magnific_generate-a-premium-ultrar_jSoVkxrLD0.png'),
  ('Under ₹1299','^Img0001.jpg'),
]

SPOTLIGHT = ['^Resizes_SP4_400_x_573_3c62f462-eb9e-4a22-913e-5c040036acd5.jpg',
             '^Resizes_SP3_400_x_573.jpg',
             '^Resizes_SP1_400_x_573_6777bb7a-9342-4354-aa46-662c19969345.jpg',
             '^Resizes_SP2_400_x_573_57f07eff-dd46-460e-8e4b-2938bf23b243.jpg']

# ---- products ---------------------------------------------------------------
# [handle, title, type, price, compare, [images], [sizes], [[colour, img], ...]]
PRODUCTS = [
["women-solid-black-ankle-length-leggings","Black Cotton Stretch Ankle Length Leggings","Ankle Length Leggings","599.00","999.00",["~files/Cat_LL-BLACK73-43.jpg","~files/Cat_LL-BLACK73-45.jpg","~files/Cat_LL-BLACK73-44.jpg","~files/Cat_LL-BLACK73-46.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-white-cotton-churidar-leggings","White Cotton Stretch Churidar","Churidar","599.00","999.00",["~files/Cat_LC-WHITE74-08.jpg","~files/Cat_LC-WHITE74-09.jpg","~files/Cat_LC-WHITE74-10.jpg","~files/Cat_LC-WHITE74-11.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-solid-black-denim-legging","Black Cotton Poly Stretch Denim Leggings","Denim Leggings","299.00","799.00",["~files/LLD-BLDN92_4.jpg","~files/LLD-BLDN92_5.jpg","~files/LLD-BLDN92_1.jpg","~files/LLD-BLDN92_3.jpg"],["S","M","L","XL","2X"],[]],
["women-solid-blue-denim-legging","Blue Cotton Poly Stretch Denim Leggings","Denim Leggings","299.00","799.00",["~files/LLD-BLUEDN89_2.jpg","~files/LLD-BLUEDN89_3.jpg","~files/LLD-BLUEDN89_4.jpg","~files/LLD-BLUEDN89_5.jpg"],["S","M","L","XL","2X"],[]],
["women-solid-black-high-rise-yoga-leggings","Black Cotton Stretch Yoga Legging","Yoga Leggings","299.00","899.00",["~files/LL06-BLACK73_2.jpg","~files/LL06-BLACK73_3.jpg","~files/LL06-BLACK73_5.jpg","~files/LL06-BLACK73_4.jpg"],["S","M","L","XL","2X"],[]],
["shimmer-leggings","Shimmer Leggings","Shimmer Leggings","299.00","799.00",["~files/LL02-ANTGLD116_3_b3c1ab34-a0d6-4803-a5f9-f0a5ccbd1b29.jpg","~files/LL02-ANTGLD116_4_c5f7fa83-a66f-412f-8a51-c5a032776d03.jpg","~files/LL02-ANTGLD116_5_a483df13-99a0-4de1-801a-eda98c5693ed.jpg","~files/LL02-ANTGLD116_6_4beaccff-7b4e-43bd-87ac-70882b6dd924.jpg"],["S","M","L","XL","2X"],[["Fuchsia","~files/1_837f4fb8-3dc5-475a-a4e9-99f26462fcc6.jpg"],["Antique Gold","~files/LL02-ANTGLD116_3_b3c1ab34-a0d6-4803-a5f9-f0a5ccbd1b29.jpg"],["Gold","~files/LL02-GOLD114_4_82ce36d9-7cc9-41af-b64b-06f7d972f531.jpg"],["Light Gold","~files/LL02-LTGOLD113_1_5ee88350-2462-4614-8088-5c9e271c9bb8.jpg"],["Copper","~files/LL02-COPPER117_3_9d399ef1-cc9d-4d47-a999-77ae06e78e84.jpg"],["Cream","~files/LL02-CREAM48_4_132e1da9-17f9-44b9-8827-1a9a81a0282c.jpg"],["White","~files/LL02-WHITE74_4_dfd66d6f-aaf5-4411-adcd-ec761ec1f6cb.jpg"],["Silver Grey","~files/LL02-SILVER115_3_56fbe9b4-f4a9-4433-a871-0672f8ed46d2.jpg"],["Black","~files/LL02-BLACK73_3_64d97ba6-bd78-4961-8238-7e8a8729dac8.jpg"],["Dark Red","~files/LL02-DKRED2_3_fe02f657-3745-4e55-b87f-e2992a847d2e.jpg"],["Maroon","~files/1_88bf355c-4539-4242-bdd4-e6f20bb587af.jpg"],["Dusty Rose","~files/LL02-DYROSE126_3_5471609f-522f-42dc-b851-0190971c457f.jpg"]]],
["women-solid-black-cotton-mid-rise-kurti-pants","Black Cotton Stretch Kurti Pants","Kurti Pants","899.00","1299.00",["~files/Cat_LPT1-BLACK73-S-01_7b83ce6f-e9f7-4085-877e-b46fa906a216.jpg","~files/Cat_LPT1-BLACK73-S-02_c1ab6832-3df6-452b-a23d-2d76e09b10b7.jpg","~files/Cat_LPT1-BLACK73-S-03_6d9060f3-d23c-4c2a-b06d-6afeaa15c969.jpg","~files/Cat_LPT1-BLACK73-S-04_24e88796-bc9a-45c8-83df-4c9b237a886a.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-solid-white-cotton-mid-rise-kurti-pants","White Cotton Stretch Kurti Pants","Kurti Pants","899.00","",["~files/Cat_LPT1-WHITE74-08.jpg","~files/Cat_LPT1-WHITE74-10.jpg","~files/Cat_LPT1-WHITE74-09.jpg","~files/Cat_LPT1-WHITE74-11.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-solid-cream-cotton-mid-rise-kurti-pants","Cream Cotton Stretch Kurti Pants","Kurti Pants","899.00","",["~files/LPT1-CREAM48_3_1247589f-61ac-4be6-beab-a2daa1d63f03.jpg","~files/LPT1-CREAM48_4_03c518d4-a31d-427d-adf6-25fb24bcc1ad.jpg","~files/LPT1-CREAM48_6_5cc20d63-252b-4330-baf3-7d4008ffcc72.jpg","~files/LPT1-CREAM48_5_4bf0402f-9f1c-4d67-b45d-9b921ab8602d.jpg"],["S","M","L","XL","2X","3X","4X"],[]],
["women-solid-navy-cotton-mid-rise-kurti-pants","Navy Cotton Stretch Kurti Pants","Kurti Pants","899.00","",["~files/1_21143066-f9ef-442e-9952-2a41e358ce59_1.jpg","~files/3_2ce7960e-ae96-4c1c-a6cf-c3a4974bca31.jpg","~files/2_9a8abca3-0f90-42ef-bbbd-521ceed477b7.jpg","~files/5_4aa11a29-dabb-4867-b74d-aff3f9442f9b_1.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-solid-maroon-cotton-mid-rise-kurti-pants","Maroon Cotton Stretch Kurti Pants","Kurti Pants","899.00","",["~files/LPT1-MARRON13_4.jpg","~files/LPT1-MARRON13_5.jpg","~files/LPT1-MARRON13_1.jpg","~files/LPT1-MARRON13.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["women-solid-wheat-cotton-mid-rise-kurti-pants","Wheat Cotton Stretch Kurti Pants","Kurti Pants","899.00","",["~files/LPT1-WHEAT44_3.jpg","~files/LPT1-WHEAT44_4.jpg","~files/LPT1-WHEAT44_5.jpg","~files/Spotlight_LPT1_8ae177d1-7355-4f90-9ef0-0e86b01c4728.jpg"],["S","M","L","XL","2X","2P","3P","4P"],[]],
["cargo-sweatpants","Cargo Sweatpants","Cargo Sweatpants","999.00","1299.00",["~files/useforcatalog_4.jpg","~files/2_7ee1f1f3-36c2-4597-9c91-03f6713ccd45.jpg","~files/1_99cb3f00-b16a-4688-905d-feb6293f3df0.jpg","~files/3_eba2db0f-29f8-4413-bf39-643814bd378f.jpg"],["XS","S","M","L","XL"],[["Pastel Blue","~files/useforcatalog_4.jpg"],["Mauve","~files/8_6331c1ff-9f4d-42d9-96d2-d412a6740511.jpg"],["Brown","~files/8_51292ff3-51db-4c94-a7cb-fea53a580a64.jpg"],["Black","~files/7_401a109c-fc84-4db3-9fdc-d943405e3ff4.jpg"],["Grey Mist","~files/7_713804fb-2f52-47a9-8de6-914ec5211638.jpg"],["Baby Pink","~files/2_1_f827d2dc-0171-41e8-ab4b-7ff012df422f.jpg"]]],
["denim-utility-pants","Denim Utility Pants","Utility Pants","1599.00","2199.00",["~files/WebsitecategoryimagesGenZ-04.jpg","~files/2_bdf492ac-7427-4808-82f6-af0c48951bba.jpg","~files/1_7b2f7d1c-96d8-4722-a7ed-7f414ea46d02.jpg","~files/3_596c78ef-67a0-491e-8755-ea76151c41ee.jpg"],["XS","S","M","L","XL"],[["Medium Blue","~files/WebsitecategoryimagesGenZ-04.jpg"],["Black","~files/9_621ae8d0-ccbb-4561-8d59-a63e6225442b.jpg"]]],
["pleated-pants","Ribbon Pants","Pleated Pants","1399.00","1999.00",["~files/useforcatalog_6.jpg","~files/2_911c901c-02c2-4e5b-aa38-8b8947f54480.jpg","~files/1_7f7a717a-b53c-45dd-9df7-d4351f8dd471.jpg","~files/3_72a4c975-7f3b-479c-9322-19a9ca7ba2d5.jpg"],["XS","S","M","L","XL"],[["Brown","~files/useforcatalog_6.jpg"],["Black","~files/7_8d1d0e82-9de0-4016-9982-83317bfd51ba.jpg"],["Light Beige","~files/9_96a842d8-f518-4752-b185-a0589826c67d.jpg"]]],
["cargo-pants","Cargo Pants","Cargo Pants","1499.00","1999.00",["~files/useforcatalog_5.jpg","~files/2_a6d3f1ae-6e99-4711-96a2-8f949822ccf7.jpg","~files/1_79c3277f-a4c5-43e6-bd79-5efc5534bcc9.jpg","~files/3_dac2173d-aa14-4061-a1da-b07d75a5d0de.jpg"],["XS","S","M","L","XL"],[["Black","~files/useforcatalog_5.jpg"],["Khaki","~files/7_dd17c499-07e6-4c11-8634-66e387c02417.jpg"],["Dark Brown","~files/7_c1976179-e1de-4350-8014-65a4ac4be7c7.jpg"],["Dark Olive","~files/1_31c45847-8f8a-4682-912e-33514f4cf310.jpg"],["Ebony Grey","~files/7_4cdfef49-8a10-4e47-8b5f-c0c5be9defe0.jpg"],["Cream","~files/Main_9c11f41d-3715-4f5e-b494-ffdfdb5869d8.jpg"]]],
["women-solid-denim-palazzos","Lyocell Denim Palazzos","Denim Palazzos","649.00","1299.00",["~files/LPZ3-BLDN92_1.jpg","~files/LPZ3-BLDN92_4.jpg","~files/LPZ3-BLDN92_5.jpg","~files/LPZ3-BLDN92_6.jpg"],["S","M","L","XL","2X","3X","4X"],[["Black","~files/LPZ3-BLDN92_1.jpg"],["Blue","~files/LPZ3-BLUEDN89_1_1.jpg"]]],
["women-basic-palazzos","Basic Palazzo","Basic Palazzos","899.00","1199.00",["~files/Cat_LPZ7-BLACK73-29_e53434f0-dd26-49b1-aa9c-78f969e496e0.jpg","~files/Cat_LPZ7-BLACK73-31_92675663-1885-4778-b368-e4252abdce33.jpg","~files/Cat_LPZ7-BLACK73-30_cdf4f3ac-f1dd-4254-9d2c-1e451c6dd7f4.jpg","~files/Cat_LPZ7-BLACK73-32_d54e21f0-b213-4979-8d02-75ac84540d4e.jpg"],["S","M","L","XL","2X"],[["Black","~files/Cat_LPZ7-BLACK73-29_e53434f0-dd26-49b1-aa9c-78f969e496e0.jpg"],["Bright Red","~files/LPZ7-BRTRED3_3_fa6bb214-863a-48dd-a62e-7f9ba02b026d.jpg"],["Dark Brown","~files/main_2e591ebd-e157-4a2c-a260-26153c5141e6.jpg"],["Ecru","~files/LPZ7-ECRU47_2_7dbf585e-ee28-45f6-a990-4346cca9b360.jpg"],["Fuchsia","~files/LPZ7-FUXIA28_2_4a88b8e9-802e-4cff-b1ee-5c972895e7ec.jpg"],["Light Beige","~files/LPZ7-LTBEIGE46_4_56bfe848-4653-44f2-8fd0-e1e3989e36c6.jpg"],["Wine","~files/2_7bd68b69-0872-4239-9582-1f786ba06796.jpg"],["Maroon","~files/LPZ7-MARRON13_3_bd41ed11-9c41-47a4-b028-384e2224470c.jpg"],["Navy","~files/LPZ7-NAVY61_3_4389d0ea-da40-4382-8ba0-81e010441a55.jpg"],["Wheat","~files/LPZ7-WHEAT44_4_2901d2e8-54fd-4d6b-a23f-3db46f5228b9.jpg"],["White","~files/Cat_LPZ7-WHITE74-SM-16_0d6d9737-39da-4b66-ba5f-8a371b1a34f2.jpg"],["Bottle Green","~files/2_a05c54f4-6fba-4010-96e8-561029f2e261.jpg"]]],
["women-black-super-stretch-jeggings","Black Cotton Polyester Super Stretch Jeggings","Super Stretch Jeggings","1299.00","1799.00",["~files/Cat_LJ03-BLACK73-15.jpg","~files/Cat_LJ03-BLACK73-17.jpg","~files/Cat_LJ03-BLACK73-16.jpg","~files/Cat_LJ03-BLACK73-18.jpg"],["XS","S","M","L","XL","2X","2P","3P"],[]],
["women-blue-slip-on-knit-jeggings","Blue Cotton Poly Stretch Knit Jeggings","Knit Jeggings","899.00","",["~files/LJ02-BLUEJEG86_2.jpg","~files/LJ02-BLUEJEG86_3.jpg","~files/LJ02-BLUEJEG86_4.jpg","~files/LJ02-BLUEJEG86_5.jpg"],["S","M","L","XL","2X"],[]],
["women-black-stripe-printed-jeggings","Black Cotton Poly Stretch Stripes Printed Jeggings","Printed Jeggings","1399.00","",["~files/LJ03-PRINT73_1.jpg","~files/LJ03-PRINT73_2.jpg","~files/LJ03-PRINT73_3.jpg","~files/LJ03-PRINT73_5.jpg"],["XS","S","M","L","XL","2X"],[]],
["women-solid-blue-denim-joggers","Blue Cotton Poly Stretch Denim Joggers","Denim Joggers","1399.00","",["~files/LJ07-BLUEDN89_3.jpg","~files/LJ07-BLUEDN89_4.jpg","~files/LJ07-BLUEDN89_5.jpg","~files/LJ07-BLUEDN89_6.jpg"],["S","M","L","XL","2X"],[]],
["cotton-stretch-track-pant","Cotton Stretch Track Pant","Track Pant","299.00","799.00",["~files/LA06-WINE167_2.jpg","~files/LA06-WINE167_3.jpg","~files/LA06-WINE167_4.jpg","~files/LA06-WINE167_5.jpg"],["S","M","L","XL","2X"],[["Antra Melange","~files/GoColors-ECommerceMay_247963_0b7b23bb-8b16-4cbb-bab8-f18c549073ab.jpg"],["Wine","~files/LA06-WINE167_2.jpg"],["Black","~files/Cat_LA06-BLACK73-15.jpg"],["Navy","~files/LA06-NAVY61_3_c05428b1-ea5b-45d7-94d6-0775ccfb8534.jpg"],["Silver Grey","~files/2_242035ad-4e36-41c1-9050-d50b175523f2.jpg"],["Dark Olive","~files/2_4c7e79d7-0a58-4e3b-a1ad-345653c6c0fd.jpg"],["Maroon","~files/2_0d5c3746-dc06-4283-b973-7a9fb5bb794c.jpg"],["Mauve","~files/2_bc6aef14-e9db-4b91-909e-fd2bd90ce0a4.jpg"]]],
["women-casual-joggers","Casual Joggers","Casual Joggers","1049.00","1399.00",["~files/LL07-BLACK73_1_68e90a0e-2563-4f74-a1c5-6b257498a770.jpg","~files/LL07-BLACK73_2_da92f223-9649-4e43-9d8d-bc5d46bf355b.jpg","~files/LL07-BLACK73_3_74204b1c-36fa-4d09-8b81-043b5a0f1621.jpg","~files/LL07-BLACK73_5_b6a8cf0e-1eab-4c4b-82c3-ea7276dd1ee1.jpg"],["S","M","L","XL","2X"],[["Black","~files/LL07-BLACK73_1_68e90a0e-2563-4f74-a1c5-6b257498a770.jpg"],["Dark Purple","~files/LL07-DKPURPL19_2_6a4033b2-2bf5-4c2f-8a5e-027f02f3c740.jpg"],["Navy","~files/LL07-NAVY61_2_58e79341-01d2-4952-9371-d4f37ddc8a23.jpg"],["Antra Melange","~files/LL07-ANTRMEL75_3_f907bdc4-a99b-4e81-aa02-ba0c4f7c4c8f.jpg"],["Olive Green","~files/LL07-OLVEGRN55_1_85aaf6e1-8cb7-4de3-911a-9c9082a06084.jpg"],["Baby Pink","~files/2_93591321-897e-4823-9f2b-384d717dc6f6.jpg"],["Brown","~files/2_6c86eea1-9ea3-4493-bd13-25bf4e1eb976.jpg"]]],
["women-cycling-shorts","Cycling Shorts","Cycling Shorts","399.00","699.00",["~files/LCYC-BLACK73_4_e0425eab-9364-4813-a3a1-5f864cd12188.jpg","~files/LCYC-BLACK73_5_931502db-9f9e-4ee9-87f3-a2a2c8eb8a26.jpg","~files/LCYC-BLACK73_1_ad2e157f-8f6e-46d7-b13d-f709aa1748c7.jpg","~files/LCYC-BLACK73_6_f3dbfbd5-3fa6-4062-a6c3-5cc06632f0ec.jpg"],["S","M","L","XL","2X"],[["Black","~files/LCYC-BLACK73_4_e0425eab-9364-4813-a3a1-5f864cd12188.jpg"],["Cream","~files/LCYC-CREAM48_3_3bd0761b-4ccd-411f-820a-4343726cbbe5.jpg"],["Navy","~files/LCYC-NAVY61_3_5617009a-42f0-4b0a-b357-2e376b4c2c38.jpg"],["Wheat","~files/LCYC-WHEAT44_1_3e689324-6951-427e-9ed4-50a0ae988a14.jpg"],["Silver Grey","~files/LCYC-SLVRGRY78_2_588c0950-f69c-40fa-8e65-40bc68150650.jpg"]]],
["casual-shorts","Casual Shorts","Casual Shorts","549.00","799.00",["~files/LSH3-BLACK73_1_36b2386a-1a38-4c29-935e-d903717ec2de.jpg","~files/LSH3-BLACK73_2_d3e9c2ef-9855-473b-9bfa-cba9132a9c69.jpg","~files/LSH3-BLACK73_3_1f1c30d5-75e0-4026-9180-f61e0e5f9300.jpg"],["S","M","L","XL","2X"],[["Black","~files/LSH3-BLACK73_1_36b2386a-1a38-4c29-935e-d903717ec2de.jpg"],["Brown","~files/2_a7cea002-9d25-4a5b-92e9-5543df424756.jpg"],["Purple","~files/2_899e81ad-7366-446a-8502-bf6167d48798.jpg"]]],
["women-solid-black-mid-rise-skinny-jeans","Black Denim Skinny Jeans","Skinny Jeans","1399.00","1899.00",["~files/LJ14-BLDN92_3.jpg","~files/LJ14-BLDN92_4.jpg","~files/LJ14-BLDN92_5.jpg"],["26","28","30","32","34","36","38"],[]],
["women-solid-blue-denim-linen-mid-rise-culottes","Blue Cotton Denim Culottes","Denim Culottes","1499.00","",["~files/Widepantsresize-02.jpg","~files/LPZ6-BLUEDN89_3.jpg","~files/LPZ6-BLUEDN89_4.jpg"],["S","M","L","XL","2X"],[]],
["salwar","Salwar","Salwar","799.00","1099.00",["~files/LSW1-CHERRY1_2_4086692d-28ce-4f58-83c7-4bec0de6ee3d.jpg","~files/LSW1-CHERRY1_3_31186c12-c0d2-4b65-8ffb-231ce861725f.jpg","~files/LSW1-CHERRY1_4_fc854d33-2b86-4470-a6f2-4fa2529365da.jpg"],["SM","LX","2X"],[["Cherry","~files/LSW1-CHERRY1_2_4086692d-28ce-4f58-83c7-4bec0de6ee3d.jpg"],["Dark Rose","~files/1_15f10c36-68bb-4306-bb07-8fd8dae23e24.jpg"],["Light Beige","~files/LSW1-LTBEIGE46_2_2d3f0e51-3563-4692-9324-2f1a53165973.jpg"],["Cream","~files/LSW1-CREAM48_4_33252bf2-ac92-4832-9cac-8f49f10d6d9f.jpg"],["Beige","~files/2_ebeaf103-ba9c-498b-8704-ae1fdfb25aa4.jpg"]]],
["women-metallic-pants","Metallic Pants","Metallic Pants","299.00","999.00",["~files/LT09-GOLD114_4_0c2b6014-73d6-4842-a65e-445152fbb5c9.jpg","~files/LT09-GOLD114_5_0473e9a8-713c-44cb-b79a-faae4bc2c358.jpg","~files/LT09-GOLD114_6_4dcb1687-1e7b-48b4-9877-ad23b3b1efee.jpg"],["S","M","L","XL","2X","2P","3P"],[["Bottle Green","~files/LT09-BOTLGRN49_3_a72c101a-03c6-491a-9a63-6518c1e84580.jpg"],["Gold","~files/LT09-GOLD114_4_0c2b6014-73d6-4842-a65e-445152fbb5c9.jpg"],["Medium Beige","~files/LT09-MBEIGE138_2_85293885-87a3-48a9-91ad-9802d76565c3.jpg"],["Light Gold","~files/LT09-LTGOLD113_3_58430e63-a97b-4986-b4e8-ee8cd48a3cf0.jpg"],["Dark Cream","~files/LT09-DKCREM121_2_63832b27-5b65-44af-afff-eb203884cbcb.jpg"],["Cream","~files/LT09-CREAM48_2_964ac29f-167b-4780-bddf-bf6c5d048dbf.jpg"],["Silver Grey","~files/LT09-SILVER115_4_50005682-79f3-405c-b0a4-2969722957ed.jpg"],["Black","~files/LT09-BLACK73_6_716534be-542e-4b63-9fe7-97abaeaefe64.jpg"],["Rust","~files/1_665f3fb6-c76b-4b0f-85c6-4aaa3c11f7ee.jpg"],["Mustard","~files/LT09-MUSTARD8_2_69b7e68e-3011-4334-b2bc-1ae2b632347f.jpg"],["Maroon","~files/LT09-MARRON13_2_12ebf4c0-673b-4906-a32a-d725a2b4434b.jpg"],["Fuchsia","~files/LT09-YGFUXIA29_3_2c05e4e9-e14a-42ae-9e71-412104f77958.jpg"]]],
["women-solid-black-viscose-harem-pants","Black Woven Viscose Harem Pant","Harem Pants","999.00","",["~files/LH02-BLACK73_2.jpg","~files/LH02-BLACK73_3.jpg","~files/LH02-BLACK73_4.jpg"],["S","M","L","XL"],[]],
["women-ikat-grey-mid-rise-printed-pencil-pant","Grey Linen Ikat Pencil Pant","Printed Pencil Pants","1399.00","",["~files/LPT2-GREY78K1_4.jpg","~files/LPT2-GREY78K1_5.jpg","~files/LPT2-GREY78K1_6.jpg"],["S","M","L","XL","2X"],[]],
["women-solid-teal-high-rise-active-shorts","Teal Nylon Stretch Active Shorts","Active Shorts","299.00","799.00",["~files/LLS3-TEAL151_3.jpg","~files/LLS3-TEAL151_4.jpg","~files/LLS3-TEAL151_1.jpg"],["S","M","L","XL","2X"],[]],
["women-solid-dusty-pink-high-rise-training-capri","Dusty Pink Poly Stretch Training Capri","Training Capri","1049.00","",["~files/LAC1-DTYPNK33_3.jpg","~files/LAC1-DTYPNK33_4.jpg","~files/LAC1-DTYPNK33_5.jpg"],["S","M","L","XL","2X"],[]],
["girls-solid-light-blue-denim-jeggings","Light Blue Denim Jeggings (Girls)","Girls Denim Jeggings","899.00","",["~files/GoColors-ECommerceMay_248467.jpg","~files/GoColors-ECommerceMay_248468.jpg","~files/GoColors-ECommerceMay_248469.jpg"],["6","8","10","12","14"],[]],
["girls-solid-blue-knit-jeggings","Blue Knit Jeggings (Girls)","Girls Knit Jeggings","299.00","549.00",["~files/GJ01-BLUEJEG86_2.jpg","~files/GJ01-BLUEJEG86_3.jpg","~files/GJ01-BLUEJEG86_4.jpg"],["6","8","10","12","14"],[]],
]

# colour name -> swatch hex, for the "Find your shade" strip and colour dots
COLOR_HEX = {
 'Black':'#111111','White':'#ffffff','Cream':'#f2e8d5','Navy':'#1f2a44','Blue':'#2f5fa8',
 'Medium Blue':'#3f6fb5','Light Blue':'#8fb6dd','Pastel Blue':'#b8cfe6','Baby Pink':'#f4c2ce',
 'Fuchsia':'#c2185b','Maroon':'#6d1f2b','Cherry':'#a11d33','Bright Red':'#d32f2f','Wine':'#5e2233',
 'Dark Rose':'#a86a78','Dusty Rose':'#c69ba3','Mauve':'#a98a9a','Purple':'#6b4a86','Dark Purple':'#4a2f5e',
 'Gold':'#d4af37','Light Gold':'#e5cd82','Antique Gold':'#bfa14a','Copper':'#b06a3b',
 'Beige':'#d8c3a5','Light Beige':'#e7d9c3','Medium Beige':'#cbb391','Dark Cream':'#eadfc6',
 'Wheat':'#dfc79a','Ecru':'#efe6d6','Khaki':'#9a8c6a','Brown':'#6b4a35','Dark Brown':'#4a3226',
 'Dark Olive':'#4d5340','Olive Green':'#6b7a4b','Bottle Green':'#1f4d3a','Teal':'#1f7a7a',
 'Grey Mist':'#c9ccce','Silver Grey':'#b9bcc0','Ebony Grey':'#4b4f54','Antra Melange':'#5b6068',
}

SHADES = ['Black','White','Navy','Cream','Fuchsia','Maroon','Olive Green','Baby Pink',
          'Wine','Beige','Teal','Silver Grey','Gold','Brown','Dark Purple','Bright Red']

REVIEWS = [
 ('Priya R.','Chennai','Fit is exactly as described — the ankle length sits perfectly on me at 5\'3". Ordered two more in other shades.',5,'Black Cotton Stretch Ankle Length Leggings'),
 ('Anjali M.','Pune','Fabric quality is the reason I keep coming back. Four washes in and no fading at all.',5,'Kurti Pants'),
 ('Sneha K.','Bengaluru','Waistband is comfortable for a full work day. Half a size down would have been better for me.',4,'Basic Palazzo'),
 ('Divya S.','Hyderabad','Cargo sweatpants are so soft. Delivery was two days ahead of the promised date.',5,'Cargo Sweatpants'),
 ('Meera T.','Mumbai','Good stretch, holds shape. Wish the plus sizes had more colour options.',4,'Super Stretch Jeggings'),
 ('Kavya N.','Kochi','Returned one size and the exchange was picked up next day. Painless.',5,'Denim Leggings'),
]

FAQ = [
 ('How do I pick the right size?','Every product page has a size chart with waist and hip measurements in inches. Our fit runs true to size; if you are between two sizes we recommend sizing up for wide pants and staying true for leggings.'),
 ('What is the return window?','30 days from delivery. Items should be unworn with tags intact. Returns and exchanges are free, and the pickup is arranged for you.'),
 ('Is Cash on Delivery available?','Yes, free COD is available on all serviceable pincodes across India. Prepaid orders get an extra 10% off at checkout.'),
 ('How long does delivery take?','Metro cities: 2–4 working days. Rest of India: 4–7 working days. You will get a tracking link by SMS and email once the order ships.'),
 ('Do you have plus sizes?','Yes. Core styles run up to 4X, and selected leggings and kurti pants are also available in 2P–4P petite-plus fits.'),
]

FOOTER = {
 'Shop':['Leggings & Churidar','Kurti Pants','Wide Pants','Jeggings','Active & Athleisure','Shorts & Capris'],
 'Company':['About us','Careers','Investor Relations','Store Locator','Blogs','Go Rewards'],
 'Help':['FAQs','Returns & Exchanges','Shipping Policy','Track Order','Size Guide','Contact Support'],
}


# ---- men & girls catalogue (captured 4 Sep 2026) ------------------------------
# same shape as PRODUCTS plus a 9th field: audience
AUDIENCE_PRODUCTS = [
["wrinkle-free-flex-knit-pants","Wrinkle Free Flex Knit Pants","Flex Knit Pants","2999.00","",["~files/2_42ac893b-fe1a-4f5c-87d1-2e0221e73aa6.jpg","~files/1_a60961ec-889b-4e8f-bcbe-dd62dbc0a9a8.jpg","~files/3_a86bd436-ec75-4845-8971-7ca19b7189a8.jpg"],["30","32","34","36","38","40"],[["Beige","~files/2_42ac893b-fe1a-4f5c-87d1-2e0221e73aa6.jpg"],["Black","~files/2_db6c4986-ce58-44c2-ad8e-2e0966b31dc2.jpg"],["Khaki","~files/1_9dbac40c-ace8-4907-b02d-7d82586fe363.jpg"],["Light Beige","~files/1_bd9d07e8-4fbe-4d4a-815a-b8281be49afc.jpg"]],"Men"],
["engineered-glide-tech-trousers","Engineered Glide Tech Trousers","Glide Tech Trousers","1499.00","",["~files/2_f4db1608-0f4d-435d-ae9d-a287e8a9a289.jpg","~files/1_0744be94-1e41-4f15-9187-9ddddeffd89f.jpg","~files/3_dd0312c1-c708-4f4c-a717-8c99114a731c.jpg"],["XS","S","M","L","XL","2X"],[["Beige","~files/2_f4db1608-0f4d-435d-ae9d-a287e8a9a289.jpg"],["Black","~files/2_d8188705-173d-497d-9040-9172fa375fc9.jpg"],["Navy","~files/2_5b90c092-c302-49f9-9e84-d75a21ad89b3.jpg"],["Olive Green","~files/2_5c226777-55e9-45d1-aada-9188fd65ba58.jpg"],["Silver Grey","~files/2_ca94f236-2d69-4508-93d6-ca5834180eac.jpg"]],"Men"],
["easeflex-lounge-pants","EaseFlex Lounge Pants","EaseFlex Lounge Pants","1299.00","",["~files/2_ff97ae9f-093f-465b-8257-402ee3668f80.jpg","~files/1_5bafa31b-fd3b-4f79-bb82-3b96a70ebe38.jpg","~files/3_e5298be2-ba8f-4480-87c5-7a200a266b85.jpg"],["XS","S","M","L","XL","2X"],[["Antra Melange","~files/2_ff97ae9f-093f-465b-8257-402ee3668f80.jpg"],["Black","~files/2_f0faa4ff-7fa8-482e-95df-6c7d6af8c8d9.jpg"],["Navy","~files/2_5da21104-e1cf-47b0-aa20-cdd37f1d2e91.jpg"],["Silver Grey","~files/2_60c3dd59-f733-4893-99e2-480f0a0dbd99.jpg"]],"Men"],
["cotton-stretch-smart-fit-pull-on-pants","Cotton Stretch Smart Fit Pull On Pants","Pull-On Pants","1999.00","",["~files/2_ba018b03-4b0f-46d7-9679-e2ae0592e53e.jpg","~files/1_bbffcc85-1053-4043-ac9a-0f26118df1be.jpg","~files/3_1ff0fa7e-daff-461f-9708-9f50fa3590d5.jpg"],["30","32","34","36","38","40"],[["Beige","~files/2_ba018b03-4b0f-46d7-9679-e2ae0592e53e.jpg"],["Black","~files/2_e2b490ad-6b4c-4849-9196-481df01c8cf4.jpg"],["Khaki","~files/2_3fc03bdd-b646-4989-916c-a5bd41203401.jpg"],["Navy","~files/2_da1a4b90-4d0c-452c-bb7f-b6ac37066618.jpg"],["Olive Green","~files/2_08e81305-08fd-4d57-bd27-70d3a89f21e3.jpg"]],"Men"],
["brushed-fabric-ultimate-chinos","Brushed Fabric Ultimate Chinos","Ultimate Chinos","1499.00","2999.00",["~files/2_cf0b401b-4b7f-4c06-b79d-32a8fca3e789.jpg","~files/1_dcae8f12-20e8-4e77-bbe6-524269ab6369.jpg","~files/3_99934152-c18f-45ff-a33d-b0319a2efe35.jpg"],["30","32","34","36","38","40"],[["Beige","~files/2_cf0b401b-4b7f-4c06-b79d-32a8fca3e789.jpg"],["Khaki","~files/2_396de31b-3595-41df-92a1-d070bad58e23.jpg"],["Light Beige","~files/2_60fc8f3a-3cef-48b6-a962-13db7088e8f4.jpg"],["Navy","~files/1_1c744070-5b88-499e-80d7-f8d3a24541b4.jpg"],["Silver Grey","~files/1_080f0816-412d-45b0-85f6-d63ffcbae583.jpg"]],"Men"],
["airlite-chinos","AirLite Chinos","Lightweight Air Chinos","2499.00","",["~files/2_abad8ed9-68c7-4bc7-a7ab-fb267cac22f1.jpg","~files/1_6eb77089-b14c-436e-b97d-2cc448a9ce61.jpg","~files/3_a7731a3c-3ff7-42ba-b180-1ef99fc9b7a0.jpg"],["30","32","34","36","38","40"],[["Beige","~files/2_abad8ed9-68c7-4bc7-a7ab-fb267cac22f1.jpg"],["Grey Mist","~files/1_ecda717c-eb08-4bca-89c7-cb5f0256b725.jpg"],["Medium Beige","~files/1_47f279bf-7a85-4d8c-9864-d9eaeff37661.jpg"],["Navy","~files/1_f2bd5b81-d5fb-4d1f-80c3-ca26466e808c.jpg"],["Olive Green","~files/1_0237bdb3-f010-4a99-8b56-3a5c0e466af0.jpg"]],"Men"],
["super-fine-2-ply-premium-cotton-shirt","Super Fine 2-Ply Premium Cotton Shirt","Premium Cotton Shirt","999.00","1999.00",["~files/1_8c34265e-d4d4-48b8-b22e-b641e801d325.jpg","~files/3_31c15151-6fb9-4d58-ae63-719ffce2b280.jpg","~files/2_a22e3ebf-b267-410a-9622-69668b47c50b.jpg"],["38","39","40","42","44","46"],[["Blue","~files/1_8c34265e-d4d4-48b8-b22e-b641e801d325.jpg"],["Bottle Green","~files/1_3b05e90e-f15c-4b52-9c99-aada0d1f15ca.jpg"],["Navy","~files/1_95152b51-3e3b-4f9d-90f3-6f595917e837.jpg"]],"Men"],
["regular-fit-casual-cotton-shirt","100% Cotton Regular Fit Casual Shirt","Casual Cotton Shirt","1299.00","",["~files/3_3397f2aa-8b52-44d3-bbf5-5bdd008f658b.jpg","~files/2_7f1933ce-7cd4-4826-abd5-5d55d46756ac.jpg","~files/1_f3bc7b34-8e0b-4d93-8d17-3e06988b94b4.jpg"],["XS","S","M","L","XL","2X"],[["Baby Pink","~files/1_f3bc7b34-8e0b-4d93-8d17-3e06988b94b4.jpg"],["Blue","~files/1_08496994-3f99-45aa-9423-2347240b07d1.jpg"],["Maroon","~files/1_00e3d1ca-4925-41ce-baa8-28958a397469.jpg"],["Silver Grey","~files/1_f1223a14-701b-464f-baff-94ad24a7c09b.jpg"]],"Men"],
["classic-pique-polo","Classic Pique Polo","Classic Pique Polo","1299.00","",["~files/2_be06f8d1-e2cb-48c4-83aa-a86b31ed32b1.jpg","~files/1_c50c08e0-2503-4ee3-9b71-6e15b4f13b48.jpg","~files/3_ba72193d-3686-4249-8b6e-b376e599a59c.jpg"],["XS","S","M","L","XL","2X"],[["Black","~files/1_0c83dbd2-a3a7-4d0f-a789-6203e0e857a6.jpg"],["Blue","~files/2_1fbdb98c-fd8e-49e9-932f-0d418e0cf3c7.jpg"],["Baby Pink","~files/3_8545ba27-af24-4f81-becc-0d3a837966e6.jpg"],["Wine","~files/2_c5a47faa-62c2-4386-ad1d-7fa0ef3b13b9.jpg"],["Dark Brown","~files/2_e001b8af-10b4-404f-aa06-5fa2304f3620.jpg"]],"Men"],
["premium-cotton-flat-knit-polo","Premium Cotton Flat Knit Polo","Flat Knit Polo","1999.00","",["~files/2_6da14326-4898-47a8-885e-2a7ebb3029ab.jpg","~files/1_49b9610f-4796-4399-ba4e-6e78f3c87fa6.jpg","~files/3_e45dca3b-49a9-4973-b1eb-a8dd126ffd4a.jpg"],["XS","S","M","L","XL","2X"],[["Beige","~files/2_6da14326-4898-47a8-885e-2a7ebb3029ab.jpg"],["White","~files/2_06c72934-f603-4786-af91-16f0f7b12dc6.jpg"],["Olive Green","~files/2_771f0aee-86a5-4b19-9b93-12970b234610.jpg"],["Navy","~files/2_9edcc514-1d22-4895-be45-0815ed492b8d.jpg"]],"Men"],
["slim-fit-jeans","Slim Fit Jeans","Slim Fit Denims","1749.00","3499.00",["~files/2_1268e78f-62d5-4b3f-9018-0ee0d868eeda.jpg","~files/1_1038244f-6f87-4155-80d2-ed425cbb5b40.jpg","~files/3_86b5f970-23a6-443e-bd56-0a09dfbb3902.jpg"],["30","32","34","36","38","40"],[["Black","~files/2_1268e78f-62d5-4b3f-9018-0ee0d868eeda.jpg"],["Light Blue","~files/2_7be35872-57a0-483d-92fe-cca2451f8bf7.jpg"],["Medium Blue","~files/2_41248868-bd3f-478d-aaf8-e861eef085f6.jpg"]],"Men"],
["classic-regular-fit-jeans","Classic Regular Fit Jeans","Regular Fit Denims","3599.00","",["~files/2_f8c784e0-abfc-49c9-84d6-bb3cb6c21b63.jpg","~files/1_664e929b-7c0c-4179-be1c-54b50cb729b6.jpg","~files/3_fc6a2d5e-d728-4597-bc88-6603f73e167b.jpg"],["30","32","34","36","38","40"],[["Blue","~files/2_f8c784e0-abfc-49c9-84d6-bb3cb6c21b63.jpg"],["Light Blue","~files/2_eb366c72-5171-4fde-b686-2a5aa420b9e8.jpg"],["Medium Blue","~files/2_8c97f969-db50-4c59-b374-310fa89408c3.jpg"]],"Men"],
["cotton-stretch-urban-cargo-shorts","Cotton Stretch Urban Cargo Shorts","Urban Cargo Shorts","1149.00","2299.00",["~files/2_06e2ccb6-3e34-45f1-a567-0a6a13258eaa.jpg","~files/1_5aee5d0e-3f57-4c76-a53b-cdf90def5378.jpg","~files/3_ce52683a-c25a-42c4-9eef-f2c868f7e466.jpg"],["30","32","34","36","38","40"],[["Beige","~files/2_2246b687-3ddd-4112-ada2-d61723b740d5.jpg"],["Khaki","~files/2_06e2ccb6-3e34-45f1-a567-0a6a13258eaa.jpg"],["Olive Green","~files/2_32464c14-853a-4a8c-b15e-360ddb9f642a.jpg"]],"Men"],
["easeflex-lounge-shorts","EaseFlex Lounge Shorts","EaseFlex Lounge Shorts","899.00","",["~files/2_8b92c077-a853-43dd-8752-611e17175315.jpg","~files/1_a05cdca6-1181-4e2a-b949-37fbdfebbaa9.jpg","~files/3_e59f4b80-3ccc-444d-91b9-00cec79befa1.jpg"],["XS","S","M","L","XL","2X"],[["Antra Melange","~files/2_8b92c077-a853-43dd-8752-611e17175315.jpg"],["Black","~files/2_49dd645f-51cf-4716-b6d6-b1a9cca2d7b3.jpg"],["Wine","~files/2_41042a44-9243-4038-9e5b-2024f671c2f0.jpg"],["Navy","~files/2_726fe82c-cddf-4d05-8446-e1b79132cbb4.jpg"]],"Men"],
["girls-solid-black-3-4th-leggings","Black Cotton Stretch Cropped Leggings","Girls 3/4th Leggings","299.00","",["~files/GLC-BLACK73_3.jpg","~files/GLC-BLACK73_4.jpg","~files/GLC-BLACK73_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-white-3-4th-leggings","White Cotton Stretch Cropped Leggings","Girls 3/4th Leggings","299.00","",["~files/GLC-WHITE74_4.jpg","~files/GLC-WHITE74_5.jpg","~files/GLC-WHITE74_1.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-blue-denim-jeggings-2","Blue Cotton Poly Stretch Denim Jeggings","Girls Denim Jeggings","899.00","",["~files/GJ03-BLUEDN89_3.jpg","~files/GJ03-BLUEDN89_4.jpg","~files/GJ03-BLUEDN89_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-light-blue-denim-jeggings-2","Light Blue Cotton Poly Stretch Denim Jeggings","Girls Denim Jeggings","899.00","",["~files/GoColors-ECommerceMay_248467.jpg","~files/GoColors-ECommerceMay_248468.jpg","~files/GoColors-ECommerceMay_248469.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-black-jeggings","Black Cotton Poly Stretch Super Stretch Jeggings","Girls Super Stretch Jeggings","799.00","",["~files/GJ02-BLACK73_5.jpg","~files/GJ02-BLACK73_4.jpg","~files/GJ02-BLACK73_3.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-black-harem-pants","Black Viscose Stretch Harem","Girls Harem Pants","499.00","",["~files/GH-BLACK73_3.jpg","~files/GH-BLACK73_4.jpg","~files/GH-BLACK73_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-navy-harem-pants","Navy Viscose Stretch Harem","Girls Harem Pants","499.00","",["~files/GH-NAVY61_3.jpg","~files/GH-NAVY61_4.jpg","~files/GH-NAVY61_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-young-fuchsia-mid-rise-knit-shorts","Young Fuchsia Cotton Knit Shorts","Girls Knit Shorts","299.00","349.00",["~files/GSH3-YGFUXIA29_3.jpg","~files/GSH3-YGFUXIA29_4.jpg","~files/GSH3-YGFUXIA29_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-solid-black-mid-rise-knit-shorts","Black Cotton Knit Shorts","Girls Knit Shorts","299.00","349.00",["~files/GSH3-BLACK73_3.jpg","~files/GSH3-BLACK73_4.jpg","~files/GSH3-BLACK73_5.jpg"],["6","8","10","12","14"],[],"Girls"],
["girls-cycling-shorts","Girls Cycling Shorts","Girls Cycling Shorts","249.00","",["~files/GCYC-NAVY61_3_c7c407ac-1d28-435c-97c0-23c3bed46e21.jpg","~files/GCYC-NAVY61_4_c16f7cd8-7d84-4dc8-8ff4-ef6cc66601ed.jpg","~files/GCYC-NAVY61_5_12290e80-0b17-4bbe-a817-db843de7018b.jpg"],["6","8","10","12","14"],[["Navy","~files/GCYC-NAVY61_3_c7c407ac-1d28-435c-97c0-23c3bed46e21.jpg"],["Black","~files/GCYC-BLACK73_3_c73d445b-2cb5-458f-bc66-a9ddf816a7f9.jpg"],["Silver Grey","~files/GCYC-SLVRGRY78_2_9f6cc59c-5ca5-47bf-9770-94469619d554.jpg"],["White","~files/1_8b9aa2c8-cbd6-4b8b-8dd4-64344effc52d.jpg"]],"Girls"],
]
PRODUCTS = PRODUCTS + AUDIENCE_PRODUCTS

# ---- L1 audiences + split banner --------------------------------------------
L1 = [('Women','women.html'),('Men','men.html'),('Girls','girls.html')]

# key: (tag, title, subtitle, cta1 label, cta1 href, cta2 label, cta2 href, disclaimer, image)
BANNERS = {
 'home': ('New Season 2026',
          'Life moves in your comfort zone',
          'Bottomwear cut for Indian body types, in fabrics that hold their shape wash '
          'after wash. XS to 4X, with petite-plus fits on core styles.',
          'Shop women', 'women.html', 'Shop men', 'men.html',
          '*Prices inclusive of all taxes. Free shipping and 30-day returns on every order. '
          'Extra 10% off applies to prepaid orders at checkout.',
          '~files/useforcatalog_6.jpg'),
 'women': ('Women · Bottomwear',
           'One fit you will reorder in six colours',
           '1200+ styles across leggings, kurti pants, palazzos and jeggings. '
           'Tested across the full size run, from XS to 4X and petite-plus 2P–4P.',
           'Shop new arrivals', 'collection.html', 'Shop best sellers', 'collection.html',
           '*Prices inclusive of all taxes. Free shipping, free COD and 30-day returns. '
           'Size availability varies by style and colour.',
           '~files/useforcatalog_5.jpg'),
 'men': ('Men · New at Go Colors',
         'Everyday tailoring, built for the commute',
         'Pants, chinos, cargos and denims in stretch fabrics that survive a full day '
         'and still press clean. Sizes 28 to 40.',
         'Shop pants & trousers', 'collection.html', 'Shop cargos', 'collection.html',
         '*Prices inclusive of all taxes. Free shipping, free COD and 30-day returns. '
         'Menswear range is stocked in selected stores and online.',
         '~files/1_c50c08e0-2503-4ee3-9b71-6e15b4f13b48.jpg'),
 'girls': ('Girls · 6 to 14 years',
           'School, play and everything after',
           'Soft cotton-stretch leggings, jeggings and pants that keep their shape '
           'through the wash cycle a school week demands.',
           'Shop leggings', 'collection.html', 'Shop jeggings', 'collection.html',
           '*Prices inclusive of all taxes. Free shipping, free COD and 30-day returns. '
           'Age guidance is indicative; check the size chart for waist and height.',
           '~files/GoColors-ECommerceMay_248467.jpg'),
}

# ---- category grid: (collection title, image, sale tag or '') -----------------
CATEGORIES = {
 'Women': [
   ('Ankle Length Leggings','^Ankle_length_churidar_550x550.jpg','Up to 40% off'),
   ('Palazzos','^Hakoba_Palazzo_550x550.jpg',''),
   ('Wide Pants','^Parachute_pant_02_550x550.jpg','New in'),
   ('Kurti Pants','^Kurti_pant_550x550.jpg',''),
   ('Skirts & Skorts','^Twill_skort_e5c57bef-0f59-4bb4-8abb-3a897654fb2c_550x550.jpg','New in'),
   ('Joggers','^Casula_jogger_550x550.jpg',''),
   ('Cargos','^Cargo_sweatpant_550x550.jpg','Flat 30% off'),
   ('Super Stretch Jeggings','^Denim_jegging_550x550.jpg',''),
   ('Ethnics','^Harem_pant_02_550x550.jpg',''),
   ('Printed Shirts','^Resizes_Printedshirts_550x550.jpg',''),
   ('Solid Shirts','^Resizes_SolidShirts_550x550.jpg',''),
   ('Short Dress','^Resizes_Shortdress_550x550.jpg','New in'),
   ('Midi Dress','^Resizes_MIDIdress_550x550.jpg',''),
   ('T-Shirts & Knit Tops','^Resizes_Tshirt_550x550.jpg',''),
   ('Blouses','^Resizes_Blouse_550x550.jpg',''),
   ('Kurti / Kurta','^Resizes_Kurta_550x550.jpg','Up to 50% off'),
 ],
 'Men': [
   ('Pants & Trousers','^Resizes_Pantsandtrouserscopy_550x550.jpg','New in'),
   ('Chinos','^Resizes_Chinoscopy_550x550.jpg','Flat 50% off'),
   ('Shirts','^Resizes_Shirtscopy_550x550.jpg','Up to 50% off'),
   ('Jeans & Denims','^Resizes_Jeanscopy_550x550.jpg','Flat 50% off'),
   ('Cargos','^Resizes_Cargopantscopy_550x550.jpg',''),
   ('Polos','^Resizes_Poloscopy_550x550.jpg','New in'),
   ('Shorts','^Resizes_Shortscopy_550x550.jpg','Up to 50% off'),
   ('T-Shirts','^Resizes_Tshirtcopy_550x550.jpg',''),
 ],
 'Girls': [
   ('Leggings','~files/GLC-BLACK73_3.jpg',''),
   ('Cropped Leggings','~files/GLC-WHITE74_4.jpg',''),
   ('Denim Jeggings','~files/GoColors-ECommerceMay_248467.jpg','New in'),
   ('Super Stretch Jeggings','~files/GJ02-BLACK73_5.jpg',''),
   ('Harem Pants','~files/GH-BLACK73_3.jpg',''),
   ('Pants','~files/GH-NAVY61_3.jpg',''),
   ('Knit Shorts','~files/GSH3-YGFUXIA29_3.jpg','Flat ₹299'),
   ('Cycling Shorts','~files/GCYC-NAVY61_3_c7c407ac-1d28-435c-97c0-23c3bed46e21.jpg',''),
 ],
}
