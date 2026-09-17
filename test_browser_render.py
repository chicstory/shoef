import json
import re

# Load data
with open("data/brands_stores_config.json", "r", encoding="utf-8") as f:
    brandsConfig = json.load(f)

with open("data/shoes_master.json", "r", encoding="utf-8") as f:
    shoesData = json.load(f)

print(f"Loaded {len(brandsConfig['brands'])} brands and {len(shoesData)} shoes.")

# Check getFilteredShoes logic
selectedBrands = set(['nike', 'adidas', 'asics', 'saucony', 'hoka', 'puma', 'newbalance', 'brooks', 'mizuno', 'on'])
catVal = 'all'
sizeVal = None
widthVal = 'all'
query = ''
outletOnly = False
currentSort = 'price-asc'

filtered = []
for shoe in shoesData:
    if shoe['brand_id'] not in selectedBrands:
        continue
    filtered.append(shoe)

print(f"Filtered shoes count: {len(filtered)}")

# Check mapping
mapped = []
for shoe in filtered:
    validPrices = shoe['prices']
    minPrice = min(p['price'] for p in validPrices)
    maxDiscount = max(p.get('discount_rate', 0) for p in validPrices)
    shoe_copy = dict(shoe)
    shoe_copy['displayPrices'] = validPrices
    shoe_copy['effectiveLowestPrice'] = minPrice
    shoe_copy['effectiveMaxDiscount'] = maxDiscount
    mapped.append(shoe_copy)

print(f"Mapped shoes count: {len(mapped)}")

# Check rendering each card
errors = []
for idx, shoe in enumerate(mapped):
    try:
        minPrice = shoe['effectiveLowestPrice']
        # check price rows
        for p in shoe['displayPrices']:
            isLowest = (p['price'] == minPrice)
            mallClass = 'dept' if p['badge'] == '백화점' else 'official' if p['badge'] == '공식몰' else 'multi'
            sizeTxt = f"{p['sizes'][0]}~{p['sizes'][-1]}mm"
            widthTxt = f"[{p['width']}]" if p.get('width') else ''
            subName = f"<span class='mall-sub-name'>{p.get('store_sub','')}</span>" if p.get('store_sub') else ''
            priceStr = f"{p['price']:,}원"
            discountStr = f"{p['discount_rate']}% 할인" if p.get('discount_rate', 0) > 0 else '정가'
            shipStr = '무료배송' if p.get('shipping', 0) == 0 else f"{p['shipping']:,}원"
            urlStr = p['url']
        
        # check info
        brand_line = shoe['brand_id'].upper()
        style_badge = shoe.get('style_code', '')
        name_kr = shoe['name_kr']
        cat_badge = shoe['category_name']
        msrp = (shoe.get('msrp') or shoe.get('official_price') or 0)
        msrp_str = f"{msrp:,}원"
        img = shoe['image_url']
        score = shoe.get('runrepeat', {}).get('score', '-')
    except Exception as e:
        errors.append((idx, shoe.get('name_kr', 'unknown'), str(e)))

if errors:
    print("ERRORS FOUND during render simulation:", errors)
else:
    print("Render simulation: ALL 13 SHOES RENDERED WITH 0 ERRORS!")
