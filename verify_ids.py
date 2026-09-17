import re

with open("app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find all getElementById
ids_in_js = re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", app_js)
print(f"Total getElementById in app.js: {len(ids_in_js)}")

missing = []
for el_id in set(ids_in_js):
    # Check if id="el_id" exists in html
    if f'id="{el_id}"' not in html and f"id='{el_id}'" not in html:
        missing.append(el_id)

if missing:
    print("MISSING IDs in HTML:", missing)
else:
    print("All getElementById exist in HTML!")
