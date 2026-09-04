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
   ('Long Dress','^Resizes_Longdress_550x550.jpg'),
   ('T-Shirts & Knit Tops','^Resizes_Tshirt_550x550.jpg'),
   ('Blouses','^Resizes_Blouse_550x550.jpg'),
   ('Kurti / Kurta','^Resizes_Kurta_550x550.jpg'),
 ],
 'Men': [
   ('Pants & Trousers','^Resizes_Pantsandtrouserscopy_550x550.jpg'),
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
["shimmer-leggings","Shimmer Leggings","Shimmer Leggings","299.00","799.00",["~files/LL02-ANTGLD116_3_b3c1ab34-a0d6-4803-a5f9-f0a5ccbd1b29.jpg","~files/LL02-ANTGLD116_4_c5f7fa83-a66f-412f-8a51-c5a032776d03.jpg","~files/LL02-ANTGLD116_5_a483df13-99a0-4de1-801a-eda98c5693ed.jpg","~files/LL02-ANTGLD116_6_4beaccff-7b4e-43bd-87ac-70882b6dd924.jpg"],["S","M","L","XL","2X"],[["Fuchsia","~files/1_837f4fb8-3dc5-475a-a4e9-99f26462fcc6.jpg"],["Antique Gold","~files/LL02-ANTGLD116_3_b3c1ab34-a0d6-4803-a5f9-f0a5ccbd1b29.jpg"],["Gold","~files/LL02-GOLD114_4_82ce36d9-7cc9-41af-b64b-06f7d972f531.jpg"],["Light Gold","~files/LL02-LTGOLD113_1_5ee88350-2462-4614-8088-5c9e271c9bb8.jpg"],["Copper","~files/LL02-COPPER117_3_9d399ef1-cc9d-4d47-a999-77ae06e78e84.jpg"],["Cream","~files/LL02-CREAM48_4_132e1da9-17f9-44b9-8827-1a9a81a0282c.jpg"]]],
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
["women-basic-palazzos","Basic Palazzo","Basic Palazzos","899.00","1199.00",["~files/Cat_LPZ7-BLACK73-29_e53434f0-dd26-49b1-aa9c-78f969e496e0.jpg","~files/Cat_LPZ7-BLACK73-31_92675663-1885-4778-b368-e4252abdce33.jpg","~files/Cat_LPZ7-BLACK73-30_cdf4f3ac-f1dd-4254-9d2c-1e451c6dd7f4.jpg","~files/Cat_LPZ7-BLACK73-32_d54e21f0-b213-4979-8d02-75ac84540d4e.jpg"],["S","M","L","XL","2X"],[["Black","~files/Cat_LPZ7-BLACK73-29_e53434f0-dd26-49b1-aa9c-78f969e496e0.jpg"],["Bright Red","~files/LPZ7-BRTRED3_3_fa6bb214-863a-48dd-a62e-7f9ba02b026d.jpg"],["Dark Brown","~files/main_2e591ebd-e157-4a2c-a260-26153c5141e6.jpg"],["Ecru","~files/LPZ7-ECRU47_2_7dbf585e-ee28-45f6-a990-4346cca9b360.jpg"],["Fuchsia","~files/LPZ7-FUXIA28_2_4a88b8e9-802e-4cff-b1ee-5c972895e7ec.jpg"],["Light Beige","~files/LPZ7-LTBEIGE46_4_56bfe848-4653-44f2-8fd0-e1e3989e36c6.jpg"]]],
["women-black-super-stretch-jeggings","Black Cotton Polyester Super Stretch Jeggings","Super Stretch Jeggings","1299.00","1799.00",["~files/Cat_LJ03-BLACK73-15.jpg","~files/Cat_LJ03-BLACK73-17.jpg","~files/Cat_LJ03-BLACK73-16.jpg","~files/Cat_LJ03-BLACK73-18.jpg"],["XS","S","M","L","XL","2X","2P","3P"],[]],
["women-blue-slip-on-knit-jeggings","Blue Cotton Poly Stretch Knit Jeggings","Knit Jeggings","899.00","",["~files/LJ02-BLUEJEG86_2.jpg","~files/LJ02-BLUEJEG86_3.jpg","~files/LJ02-BLUEJEG86_4.jpg","~files/LJ02-BLUEJEG86_5.jpg"],["S","M","L","XL","2X"],[]],
["women-black-stripe-printed-jeggings","Black Cotton Poly Stretch Stripes Printed Jeggings","Printed Jeggings","1399.00","",["~files/LJ03-PRINT73_1.jpg","~files/LJ03-PRINT73_2.jpg","~files/LJ03-PRINT73_3.jpg","~files/LJ03-PRINT73_5.jpg"],["XS","S","M","L","XL","2X"],[]],
["women-solid-blue-denim-joggers","Blue Cotton Poly Stretch Denim Joggers","Denim Joggers","1399.00","",["~files/LJ07-BLUEDN89_3.jpg","~files/LJ07-BLUEDN89_4.jpg","~files/LJ07-BLUEDN89_5.jpg","~files/LJ07-BLUEDN89_6.jpg"],["S","M","L","XL","2X"],[]],
["cotton-stretch-track-pant","Cotton Stretch Track Pant","Track Pant","299.00","799.00",["~files/LA06-WINE167_2.jpg","~files/LA06-WINE167_3.jpg","~files/LA06-WINE167_4.jpg","~files/LA06-WINE167_5.jpg"],["S","M","L","XL","2X"],[["Antra Melange","~files/GoColors-ECommerceMay_247963_0b7b23bb-8b16-4cbb-bab8-f18c549073ab.jpg"],["Wine","~files/LA06-WINE167_2.jpg"],["Black","~files/Cat_LA06-BLACK73-15.jpg"],["Navy","~files/LA06-NAVY61_3_c05428b1-ea5b-45d7-94d6-0775ccfb8534.jpg"],["Silver Grey","~files/2_242035ad-4e36-41c1-9050-d50b175523f2.jpg"],["Dark Olive","~files/2_4c7e79d7-0a58-4e3b-a1ad-345653c6c0fd.jpg"]]],
["women-casual-joggers","Casual Joggers","Casual Joggers","1049.00","1399.00",["~files/LL07-BLACK73_1_68e90a0e-2563-4f74-a1c5-6b257498a770.jpg","~files/LL07-BLACK73_2_da92f223-9649-4e43-9d8d-bc5d46bf355b.jpg","~files/LL07-BLACK73_3_74204b1c-36fa-4d09-8b81-043b5a0f1621.jpg","~files/LL07-BLACK73_5_b6a8cf0e-1eab-4c4b-82c3-ea7276dd1ee1.jpg"],["S","M","L","XL","2X"],[["Black","~files/LL07-BLACK73_1_68e90a0e-2563-4f74-a1c5-6b257498a770.jpg"],["Dark Purple","~files/LL07-DKPURPL19_2_6a4033b2-2bf5-4c2f-8a5e-027f02f3c740.jpg"],["Navy","~files/LL07-NAVY61_2_58e79341-01d2-4952-9371-d4f37ddc8a23.jpg"],["Antra Melange","~files/LL07-ANTRMEL75_3_f907bdc4-a99b-4e81-aa02-ba0c4f7c4c8f.jpg"],["Olive Green","~files/LL07-OLVEGRN55_1_85aaf6e1-8cb7-4de3-911a-9c9082a06084.jpg"],["Baby Pink","~files/2_93591321-897e-4823-9f2b-384d717dc6f6.jpg"]]],
["women-cycling-shorts","Cycling Shorts","Cycling Shorts","399.00","699.00",["~files/LCYC-BLACK73_4_e0425eab-9364-4813-a3a1-5f864cd12188.jpg","~files/LCYC-BLACK73_5_931502db-9f9e-4ee9-87f3-a2a2c8eb8a26.jpg","~files/LCYC-BLACK73_1_ad2e157f-8f6e-46d7-b13d-f709aa1748c7.jpg","~files/LCYC-BLACK73_6_f3dbfbd5-3fa6-4062-a6c3-5cc06632f0ec.jpg"],["S","M","L","XL","2X"],[["Black","~files/LCYC-BLACK73_4_e0425eab-9364-4813-a3a1-5f864cd12188.jpg"],["Cream","~files/LCYC-CREAM48_3_3bd0761b-4ccd-411f-820a-4343726cbbe5.jpg"],["Navy","~files/LCYC-NAVY61_3_5617009a-42f0-4b0a-b357-2e376b4c2c38.jpg"],["Wheat","~files/LCYC-WHEAT44_1_3e689324-6951-427e-9ed4-50a0ae988a14.jpg"],["Silver Grey","~files/LCYC-SLVRGRY78_2_588c0950-f69c-40fa-8e65-40bc68150650.jpg"]]],
["casual-shorts","Casual Shorts","Casual Shorts","549.00","799.00",["~files/LSH3-BLACK73_1_36b2386a-1a38-4c29-935e-d903717ec2de.jpg","~files/LSH3-BLACK73_2_d3e9c2ef-9855-473b-9bfa-cba9132a9c69.jpg","~files/LSH3-BLACK73_3_1f1c30d5-75e0-4026-9180-f61e0e5f9300.jpg"],["S","M","L","XL","2X"],[["Black","~files/LSH3-BLACK73_1_36b2386a-1a38-4c29-935e-d903717ec2de.jpg"],["Brown","~files/2_a7cea002-9d25-4a5b-92e9-5543df424756.jpg"],["Purple","~files/2_899e81ad-7366-446a-8502-bf6167d48798.jpg"]]],
["women-solid-black-mid-rise-skinny-jeans","Black Denim Skinny Jeans","Skinny Jeans","1399.00","1899.00",["~files/LJ14-BLDN92_3.jpg","~files/LJ14-BLDN92_4.jpg","~files/LJ14-BLDN92_5.jpg"],["26","28","30","32","34","36","38"],[]],
["women-solid-blue-denim-linen-mid-rise-culottes","Blue Cotton Denim Culottes","Denim Culottes","1499.00","",["~files/Widepantsresize-02.jpg","~files/LPZ6-BLUEDN89_3.jpg","~files/LPZ6-BLUEDN89_4.jpg"],["S","M","L","XL","2X"],[]],
["salwar","Salwar","Salwar","799.00","1099.00",["~files/LSW1-CHERRY1_2_4086692d-28ce-4f58-83c7-4bec0de6ee3d.jpg","~files/LSW1-CHERRY1_3_31186c12-c0d2-4b65-8ffb-231ce861725f.jpg","~files/LSW1-CHERRY1_4_fc854d33-2b86-4470-a6f2-4fa2529365da.jpg"],["SM","LX","2X"],[["Cherry","~files/LSW1-CHERRY1_2_4086692d-28ce-4f58-83c7-4bec0de6ee3d.jpg"],["Dark Rose","~files/1_15f10c36-68bb-4306-bb07-8fd8dae23e24.jpg"],["Light Beige","~files/LSW1-LTBEIGE46_2_2d3f0e51-3563-4692-9324-2f1a53165973.jpg"],["Cream","~files/LSW1-CREAM48_4_33252bf2-ac92-4832-9cac-8f49f10d6d9f.jpg"],["Beige","~files/2_ebeaf103-ba9c-498b-8704-ae1fdfb25aa4.jpg"]]],
["women-metallic-pants","Metallic Pants","Metallic Pants","299.00","999.00",["~files/LT09-GOLD114_4_0c2b6014-73d6-4842-a65e-445152fbb5c9.jpg","~files/LT09-GOLD114_5_0473e9a8-713c-44cb-b79a-faae4bc2c358.jpg","~files/LT09-GOLD114_6_4dcb1687-1e7b-48b4-9877-ad23b3b1efee.jpg"],["S","M","L","XL","2X","2P","3P"],[["Bottle Green","~files/LT09-BOTLGRN49_3_a72c101a-03c6-491a-9a63-6518c1e84580.jpg"],["Gold","~files/LT09-GOLD114_4_0c2b6014-73d6-4842-a65e-445152fbb5c9.jpg"],["Medium Beige","~files/LT09-MBEIGE138_2_85293885-87a3-48a9-91ad-9802d76565c3.jpg"],["Light Gold","~files/LT09-LTGOLD113_3_58430e63-a97b-4986-b4e8-ee8cd48a3cf0.jpg"],["Dark Cream","~files/LT09-DKCREM121_2_63832b27-5b65-44af-afff-eb203884cbcb.jpg"]]],
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
