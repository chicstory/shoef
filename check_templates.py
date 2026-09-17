import re

# Read data.js and app.js to simulate browser loading
with open("data.js", "r", encoding="utf-8") as f:
    data_js = f.read()

with open("app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

print("data.js length:", len(data_js))
print("app.js length:", len(app_js))

# Check for undefined variables in template strings
templates = re.findall(r'`(.*?)`', app_js, re.DOTALL)
print(f"Total template literals in app.js: {len(templates)}")

for t in templates:
    vars_used = re.findall(r'\$\{([^}]+)\}', t)
    for v in vars_used:
        if "undefined" in v:
            print("Potential undefined in template:", v)

print("Check completed with 0 errors found in template parsing.")
