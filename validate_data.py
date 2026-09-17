import json

with open("data/shoes_master.json", "r", encoding="utf-8") as f:
    shoes = json.load(f)

print(f"=== VERIFIED PRODUCTS LIST IN HTML ({len(shoes)} items) ===")
for i, s in enumerate(shoes):
    p = s["prices"][0]
    print(f"[{i+1}] [{s['brand_id'].upper()}] {s['name_kr']}")
    print(f"    카테고리: {s['category_name']} | 정가: {s['msrp']:,}원 -> 실시간판매가: {p['price']:,}원 ({p['discount_rate']}% 할인)")
    print(f"    발볼: {s['widths']} | 재고사이즈: {p['sizes'][0]}~{p['sizes'][-1]}mm")
    print(f"    실제 PDP 링크: {p['url']}")
