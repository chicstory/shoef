"""
RunRepeat Quarterly New Release & Version Bump Scanner
======================================================
Automated audit tool to discover newly released running shoes, next-generation 
version bumps (e.g. v22 -> v23), and new model lines across the 10 major brands.

Usage:
    python check_runrepeat_new_releases.py
    python check_runrepeat_new_releases.py --brand brooks
    python check_runrepeat_new_releases.py --summary-only
"""

import sys
import os
import re
import json
import time
import argparse
import urllib.request
from datetime import datetime

# Windows Console UTF-8 safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BRAND_CATALOG_URLS = {
    "adidas": "https://runrepeat.com/adidas-running-shoes?order=newest",
    "nike": "https://runrepeat.com/nike-running-shoes?order=newest",
    "asics": "https://runrepeat.com/asics-running-shoes?order=newest",
    "saucony": "https://runrepeat.com/saucony-running-shoes?order=newest",
    "hoka": "https://runrepeat.com/hoka-running-shoes?order=newest",
    "newbalance": "https://runrepeat.com/new-balance-running-shoes?order=newest",
    "puma": "https://runrepeat.com/puma-running-shoes?order=newest",
    "mizuno": "https://runrepeat.com/mizuno-running-shoes?order=newest",
    "brooks": "https://runrepeat.com/brooks-running-shoes?order=newest",
    "on": "https://runrepeat.com/on-running-shoes?order=newest",
}

def clean_slug(url_or_slug: str) -> str:
    """Extract and normalize shoe slug from URL."""
    slug = url_or_slug.split("/")[-1].strip().lower()
    slug = re.sub(r'[\?#].*$', '', slug)
    return slug

def extract_generation_number(name_or_slug: str):
    """Extract numeric generation or version number if present (e.g., 25 from Ghost 25 or v6)."""
    # Matches 'v-6', 'v6', or standalone numbers like '24', '41'
    v_match = re.search(r'\bv-?(\d+)\b', name_or_slug, re.IGNORECASE)
    if v_match:
        return int(v_match.group(1))
    num_matches = re.findall(r'\b(\d+)\b', name_or_slug)
    if num_matches:
        # Filter out years like 2024, 2025, 2026
        valid = [int(n) for n in num_matches if int(n) < 100]
        if valid:
            return valid[-1]
    return None

def fetch_brand_catalog(brand_id: str, url: str):
    """Fetch and parse products and scores from RunRepeat brand catalog."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ko;q=0.8"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  [ERROR] Failed to fetch {url}: {e}", file=sys.stderr)
        return []

    # 1. Parse JSON-LD ItemList
    items = []
    ld_matches = re.findall(r'<script type="application/ld\+json">([^<]+)</script>', html)
    for m in ld_matches:
        try:
            data = json.loads(m)
            if data.get("@type") == "ItemList":
                for it in data.get("itemListElement", []):
                    name = it.get("name", "").strip()
                    item_url = it.get("url", "").strip()
                    if name and item_url:
                        items.append({
                            "name": name,
                            "url": item_url,
                            "slug": clean_slug(item_url),
                            "score": None
                        })
        except Exception:
            pass

    # 2. Extract scores from HTML cards
    score_pattern = r'<div class="product-name"[^>]*>\s*<a href="([^"]+)"[^>]*>\s*<span[^>]*>([^<]+)</span>.*?corescore-big__score"[^>]*>(\d+)</div>'
    score_map = {}
    for href, card_name, score in re.findall(score_pattern, html, re.DOTALL):
        slug = clean_slug(href)
        score_map[slug] = int(score)

    # Attach scores
    for it in items:
        if it["slug"] in score_map:
            it["score"] = score_map[it["slug"]]

    return items

def analyze_against_database(tracked_shoes, catalog_items, brand_id):
    """
    Compare RunRepeat catalog items with currently tracked shoes in database.
    Categorizes into:
      - TRACKED: Already in DB
      - VERSION_BUMP: Series exists with an older number in DB (e.g. Ghost 17 -> Ghost 18)
      - NEW_MODEL: Brand new line / series (e.g. Revel Max, Cloudboom Strike)
    """
    brand_tracked = [s for s in tracked_shoes if s.get("brand_id") == brand_id]
    
    # Map of series and max version in current DB
    tracked_slugs = set(clean_slug(s.get("runrepeat", {}).get("url", s.get("id", ""))) for s in brand_tracked)
    
    series_map = {}
    for s in brand_tracked:
        name_en = s.get("name_en", "")
        ver = extract_generation_number(name_en)
        # Extract series base words from English name (strip brand and version number)
        clean_name = re.sub(r'^(adidas|nike|asics|saucony|hoka|new\s*balance|puma|mizuno|brooks|on)\s+', '', name_en, flags=re.IGNORECASE)
        clean_base = re.sub(r'\b(v-?\d+|\d+)\b', '', clean_name, flags=re.IGNORECASE).strip().lower()
        clean_base = re.sub(r'\s+', ' ', clean_base)
        
        if clean_base:
            if clean_base not in series_map or (ver and ver > series_map[clean_base]["max_ver"]):
                series_map[clean_base] = {
                    "max_ver": ver or 0,
                    "sample_shoe": name_en
                }

    results = []
    for item in catalog_items:
        slug = item["slug"]
        name = item["name"]
        item_ver = extract_generation_number(name)
        
        # Check direct match
        is_direct_match = any(slug in ts or ts in slug for ts in tracked_slugs)
        
        status = "TRACKED"
        note = "Already tracked in database"
        
        if not is_direct_match:
            # Check if this is a version bump of an existing series
            bump_found = False
            item_clean_name = re.sub(r'^(adidas|nike|asics|saucony|hoka|new\s*balance|puma|mizuno|brooks|on)\s+', '', name, flags=re.IGNORECASE).lower()
            
            for base_word, info in series_map.items():
                if base_word in item_clean_name:
                    if item_ver and item_ver > info["max_ver"]:
                        status = "VERSION_BUMP"
                        note = f"Bump detected: DB has {info['sample_shoe']} (v{info['max_ver']}) -> RunRepeat has {name} (v{item_ver})"
                        bump_found = True
                        break
                    elif item_ver == info["max_ver"]:
                        status = "TRACKED"
                        note = f"Matches tracked generation ({info['sample_shoe']})"
                        bump_found = True
                        break
            if not bump_found:
                status = "NEW_MODEL"
                note = f"New model line or unindexed variant: {name}"

        results.append({
            "name": name,
            "url": item["url"],
            "slug": slug,
            "score": item["score"],
            "status": status,
            "note": note
        })

    return results

def run_quarterly_scanner(target_brand=None, summary_only=False):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    master_json_path = os.path.join(base_dir, "data", "shoes_master.json")
    
    if not os.path.exists(master_json_path):
        print(f"[ERROR] {master_json_path} not found. Run generate_wiki_master.py first.", file=sys.stderr)
        sys.exit(1)

    with open(master_json_path, "r", encoding="utf-8") as f:
        tracked_shoes = json.load(f)

    print("=" * 75)
    print(" [ShoeF Wiki] RunRepeat Quarterly New Release & Bump Scanner")
    print(f" Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" Current Database: {len(tracked_shoes)} verified models across 10 brands")
    print("=" * 75)

    brands_to_scan = [target_brand] if target_brand else list(BRAND_CATALOG_URLS.keys())
    
    full_audit_report = {
        "audit_timestamp": datetime.now().isoformat(),
        "total_tracked_in_db": len(tracked_shoes),
        "brands_audited": brands_to_scan,
        "summary": {
            "version_bumps_count": 0,
            "new_models_count": 0,
            "already_tracked_count": 0
        },
        "brand_details": {}
    }

    total_bumps = 0
    total_new = 0

    for brand_id in brands_to_scan:
        url = BRAND_CATALOG_URLS.get(brand_id)
        if not url:
            print(f"Unknown brand: {brand_id}")
            continue

        print(f"\n>> Scanning [{brand_id.upper()}] via {url} ...")
        items = fetch_brand_catalog(brand_id, url)
        time.sleep(0.4) # Polite throttle

        if not items:
            print(f"  [WARN] No catalog items retrieved for {brand_id}.")
            continue

        analysis = analyze_against_database(tracked_shoes, items, brand_id)
        
        bumps = [r for r in analysis if r["status"] == "VERSION_BUMP"]
        new_models = [r for r in analysis if r["status"] == "NEW_MODEL"]
        tracked = [r for r in analysis if r["status"] == "TRACKED"]

        total_bumps += len(bumps)
        total_new += len(new_models)

        full_audit_report["brand_details"][brand_id] = {
            "total_scanned": len(items),
            "version_bumps": bumps,
            "new_models": new_models,
            "tracked": tracked
        }

        print(f"  + Found {len(items)} releases (Bumps: {len(bumps)}, New Lines: {len(new_models)}, Tracked: {len(tracked)})")

        if not summary_only:
            if bumps:
                print("    [VERSION BUMP CANDIDATES]:")
                for b in bumps[:5]:
                    score_str = f"Score: {b['score']}" if b['score'] else "Score: Pending"
                    print(f"       * {b['name']} ({score_str}) -> {b['note']}")
            if new_models:
                print("    [NEW MODEL CANDIDATES]:")
                for n in new_models[:5]:
                    score_str = f"Score: {n['score']}" if n['score'] else "Score: Pending"
                    print(f"       * {n['name']} ({score_str}) -> {n['url']}")

    full_audit_report["summary"]["version_bumps_count"] = total_bumps
    full_audit_report["summary"]["new_models_count"] = total_new

    # Save structured audit file
    audit_file_path = os.path.join(base_dir, "data", "runrepeat_quarterly_audit.json")
    with open(audit_file_path, "w", encoding="utf-8") as f:
        json.dump(full_audit_report, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(" [COMPLETE] Quarterly Audit Complete!")
    print(f" Summary: {total_bumps} Version Bumps | {total_new} New Model Candidates detected")
    print(f" Full Report Saved: {audit_file_path}")
    print("=" * 75)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RunRepeat Quarterly New Release Scanner")
    parser.add_argument("--brand", help="Target specific brand (e.g. adidas, brooks, saucony)")
    parser.add_argument("--summary-only", action="store_true", help="Print only summary counts")
    args = parser.parse_args()

    run_quarterly_scanner(target_brand=args.brand, summary_only=args.summary_only)
