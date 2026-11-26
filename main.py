LINE = "The self-checkout scanned my kale, paused, and printed 'unexpected item in bagging area' — which is also what my therapist said about my life choices."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
with open(path, encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match the line"
