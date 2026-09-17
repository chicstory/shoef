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
        assert "prices" in s and len(s["prices"]) > 0
        for p in s["prices"]:
            assert "price" in p and "store_name" in p and "sizes" in p

    print(" -> All shoes schema and prices verified 100% successfully!")

if __name__ == "__main__":
    verify_data()
