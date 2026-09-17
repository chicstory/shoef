import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "index_template.html")
app_js_path = os.path.join(base_dir, "app.js")
index_html_path = os.path.join(base_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

with open(app_js_path, "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace <script src="app.js"></script> with inline script
bundled_html = template.replace('<script src="app.js"></script>', f'<script>\n{app_js}\n  </script>')

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(bundled_html)

print(f"Successfully generated single self-contained index.html ({len(bundled_html)} bytes)!")
