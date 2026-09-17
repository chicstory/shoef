import os
import subprocess
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "index.html")
file_url = f"file:///{html_path.replace(os.sep, '/')}"

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]
chrome_bin = None
for p in chrome_paths:
    if os.path.exists(p):
        chrome_bin = p
        break

if not chrome_bin:
    print("Chrome not found for headless screenshot.")
    exit(0)

# 1. Desktop Screenshot (1280x900)
desktop_png = os.path.join(base_dir, "desktop_expanded.png")
cmd1 = [
    chrome_bin,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,900",
    f"--screenshot={desktop_png}",
    file_url
]
subprocess.run(cmd1, capture_output=True)
print("Desktop screenshot saved:", os.path.exists(desktop_png))

# 2. Mobile Screenshot (360x740)
mobile_png = os.path.join(base_dir, "mobile_expanded.png")
cmd2 = [
    chrome_bin,
    "--headless",
    "--disable-gpu",
    "--window-size=360,740",
    f"--screenshot={mobile_png}",
    file_url
]
subprocess.run(cmd2, capture_output=True)
print("Mobile screenshot saved:", os.path.exists(mobile_png))
