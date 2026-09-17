import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "index_template.html")
style_css_path = os.path.join(base_dir, "style.css")
app_js_path = os.path.join(base_dir, "app.js")
index_html_path = os.path.join(base_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

with open(style_css_path, "r", encoding="utf-8") as f:
    style_css = f.read()

with open(app_js_path, "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace <link rel="stylesheet" href="style.css"> with inline style
bundled_html = template.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{style_css}\n  </style>')

# Replace <script src="app.js"></script> with inline script
bundled_html = bundled_html.replace('<script src="app.js"></script>', f'<script>\n{app_js}\n  </script>')

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(bundled_html)

print(f"Successfully generated single self-contained index.html with inlined CSS & JS ({len(bundled_html)} bytes)!")
