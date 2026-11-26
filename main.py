"""Frost Worst Pizza: writes one funny pitch line to entry.txt.

The pitch sells a genuinely terrible topping (soggy cereal on pizza)
with a concrete image and a surprise turn at the end.
"""

import os

LINE = "Introducing soggy-cereal pizza: milk-soaked cornflakes drowning in tomato sauce \u2014 breakfast and regret in every bite, crunch sold separately."

# The gate requires 1-200 characters of non-whitespace text.
assert 1 <= len(LINE.strip()) <= 200, f"line is {len(LINE)} chars"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
