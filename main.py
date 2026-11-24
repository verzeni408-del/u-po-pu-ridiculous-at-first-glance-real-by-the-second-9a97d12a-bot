import os

# One-sentence startup pitch, written exactly as-is: a single sentence
# with no trailing newline, so the output stays within the 200-char limit.
ENTRY = "We bury dead houseplants in tiny coffins with a printed eulogy, $29 a plant, because guilt is the only subscription that never churns."

out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
