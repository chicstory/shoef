import re

# Read index.html and app.js
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Remove external script tags from index.html
html = re.sub(r'<script src="data.js[^"]*"></script>\s*', '', html)
html = re.sub(r'<script src="app.js[^"]*"></script>\s*', '', html)

# Remove the visual error logger from head
html = re.sub(r'<!-- Visual Error Logger \(디버그용\) -->.*?window\.onerror.*?</script>\s*', '', html, flags=re.DOTALL)

# Insert inline script right before </body>
inline_script = f"""
  <script>
{app_js}
  </script>
</body>
"""

html = html.replace("</body>", inline_script)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully inlined app.js into index.html! No external JS files needed!")
