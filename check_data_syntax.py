with open("data.js", "r", encoding="utf-8") as f:
    code = f.read()

print(f"data.js total chars: {len(code)}")

# Let's find where window.SHOEF_CONFIG is assigned
p1 = code.find("window.SHOEF_CONFIG = ")
p2 = code.find("window.SHOEF_DATA = ")
p3 = code.find("window.SHOEF_MASTER = ")

print("p1 (CONFIG):", p1)
print("p2 (DATA):", p2)
print("p3 (MASTER):", p3)

if p1 != -1 and p2 != -1:
    config_str = code[p1 + len("window.SHOEF_CONFIG = "):p2].strip()
    if config_str.endswith(";"):
        config_str = config_str[:-1].strip()
    import json
    try:
        cfg = json.loads(config_str)
        print("Config JSON parsed successfully! Keys:", list(cfg.keys()))
    except Exception as e:
        print("Config JSON PARSE ERROR:", e)
        print("Tail of config_str:", repr(config_str[-100:]))

if p2 != -1 and p3 != -1:
    data_str = code[p2 + len("window.SHOEF_DATA = "):p3].strip()
    if data_str.endswith(";"):
        data_str = data_str[:-1].strip()
    try:
        data = json.loads(data_str)
        print("Data JSON parsed successfully! Total items:", len(data))
    except Exception as e:
        print("Data JSON PARSE ERROR:", e)
        print("Tail of data_str:", repr(data_str[-100:]))
