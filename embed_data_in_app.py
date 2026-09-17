import json

with open("data/brands_stores_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

with open("data/shoes_master.json", "r", encoding="utf-8") as f:
    shoes = json.load(f)

print(f"Embedding {len(config['brands'])} brands and {len(shoes)} shoes directly into app.js...")

with open("app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace the data loading section in app.js with embedded data
config_json_str = json.dumps(config, ensure_ascii=False, indent=2)
shoes_json_str = json.dumps(shoes, ensure_ascii=False, indent=2)

embedded_header = f"""/**
 * ShoeF Wiki & Price - Main Application Controller (Fully Self-Contained)
 * 100% Verified Real Products from TheHyundai SmartStore
 */

// Embedded Fallback Data (Guarantees 0-latency instant render in file:// protocol)
const EMBEDDED_CONFIG = {config_json_str};
const EMBEDDED_SHOES = {shoes_json_str};

"""

# Find where initShoeFApp starts
idx = app_js.find("async function initShoeFApp()")
if idx == -1:
    idx = app_js.find("function initShoeFApp()")

# Find where load data ends (around initBrandCheckboxes)
init_idx = app_js.find("initBrandCheckboxes();")

# Everything after init_idx
after_init = app_js[init_idx:]

new_app_js = embedded_header + f"""function initShoeFApp() {{
  let brandsConfig = EMBEDDED_CONFIG;
  let shoesData = EMBEDDED_SHOES;
  let selectedBrands = new Set(['nike', 'adidas', 'asics', 'saucony', 'hoka', 'puma', 'newbalance', 'brooks', 'mizuno', 'on']);
  let currentSort = 'price-asc';

  // DOM Elements
  const brandGridEl = document.getElementById('brandCheckboxGrid');
  const btnSelectAllBrands = document.getElementById('btnSelectAllBrands');
  const btnDeselectAllBrands = document.getElementById('btnDeselectAllBrands');
  const categoryFilter = document.getElementById('categoryFilter');
  const sizeFilter = document.getElementById('sizeFilter');
  const widthFilter = document.getElementById('widthFilter');
  const searchKeyword = document.getElementById('searchKeyword');
  const outletOnlyToggle = document.getElementById('outletOnlyToggle');
  const totalCountEl = document.getElementById('totalCount');
  const shoesListEl = document.getElementById('shoesList');
  const sortBtns = document.querySelectorAll('.sort-btn');

  // Modal Elements
  const modalEl = document.getElementById('runrepeatModal');
  const btnCloseModal = document.getElementById('btnCloseModal');
  const modalBrandBadge = document.getElementById('modalBrandBadge');
  const modalShoeName = document.getElementById('modalShoeName');
  const modalScore = document.getElementById('modalScore');
  const modalWeight = document.getElementById('modalWeight');
  const modalDrop = document.getElementById('modalDrop');
  const modalStack = document.getElementById('modalStack');
  const modalPlate = document.getElementById('modalPlate');
  const modalFoam = document.getElementById('modalFoam');
  const modalProsList = document.getElementById('modalProsList');
  const modalConsList = document.getElementById('modalConsList');
  const modalSummary = document.getElementById('modalSummary');

  // If window data is provided, prefer it
  if (typeof window !== 'undefined') {{
    if (window.SHOEF_CONFIG) brandsConfig = window.SHOEF_CONFIG;
    if (window.SHOEF_DATA || window.SHOEF_MASTER) shoesData = window.SHOEF_DATA || window.SHOEF_MASTER;
  }}

  // 2. Init Controls
  {after_init}
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(new_app_js)

print("Successfully generated fully self-contained app.js!")
