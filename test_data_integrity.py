import json
import os
import sys

def verify_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "data", "brands_stores_config.json")
    shoes_path = os.path.join(base_dir, "data", "shoes_master.json")

    print(f"[TEST] Checking config: {config_path}")
    assert os.path.exists(config_path), "brands_stores_config.json missing"
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    assert len(config["brands"]) == 10, f"Expected 10 brands, got {len(config['brands'])}"
    assert config["sizes"][0] == 230, f"Size must start from 230, got {config['sizes'][0]}"
    print(f" -> 10 brands & size range (230~{config['sizes'][-1]}) OK")

    print(f"[TEST] Checking shoes: {shoes_path}")
    assert os.path.exists(shoes_path), "shoes_master.json missing"
    with open(shoes_path, "r", encoding="utf-8") as f:
        shoes = json.load(f)

    print(f" -> Total shoes models loaded: {len(shoes)}")
    for s in shoes:
        assert "id" in s and "brand_id" in s and "name_kr" in s
        assert "category" in s
        assert "runrepeat" in s
        rr = s["runrepeat"]
        assert "score" in rr
        assert "pros" in rr and len(rr["pros"]) > 0
        assert "cons" in rr and len(rr["cons"]) > 0
        assert "msrp_krw" in s and s["msrp_krw"] > 0
        assert "msrp_usd" in s and s["msrp_usd"] > 0
        if "prices" in s and s["prices"]:
            for p in s["prices"]:
                assert "price" in p and "store_name" in p and "sizes" in p

    print(" -> All shoes schema and prices verified 100% successfully!")

    # 4. Affiliate Links Integrity Check (Shield against quarterly data wipeout)
    affiliates_path = os.path.join(base_dir, "data", "affiliates.json")
    if os.path.exists(affiliates_path):
        print(f"[TEST] Checking affiliate mappings: {affiliates_path}")
        with open(affiliates_path, "r", encoding="utf-8") as f:
            aff_map = json.load(f)
        
        shoes_dict = {s["id"]: s for s in shoes}
        for shoe_id, aff_info in aff_map.items():
            assert shoe_id in shoes_dict, f"[ERROR] Affiliate target shoe '{shoe_id}' not found in shoes_master.json!"
            target_shoe = shoes_dict[shoe_id]
            assert "affiliate" in target_shoe, f"[ERROR] Affiliate link missing in shoe '{shoe_id}'!"
            assert target_shoe["affiliate"].get("url") == aff_info["url"], f"[ERROR] Affiliate URL mismatch in shoe '{shoe_id}'!"
        print(f" -> {len(aff_map)} affiliate link(s) verified and shielded against wipeout OK")

if __name__ == "__main__":
    verify_data()
