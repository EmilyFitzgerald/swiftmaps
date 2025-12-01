import os
import json

MAP_DIR = "docs/maps"
OUT_FILE = os.path.join(MAP_DIR, "list.json")

files = [f for f in os.listdir(MAP_DIR) if f.endswith(".html")]

with open(OUT_FILE, "w") as f:
    json.dump(files, f, indent=2)

print(f"✓ Updated {OUT_FILE} with {len(files)} map(s).")
