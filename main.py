import os

# One-sentence entry, written exactly as-is: no trailing newline,
# so the file stays within the competition's 200-character limit.
ENTRY = "We sell sick-day excuses vetted by a retired detective, $5 each, because HR believes a good alibi more than a bad cough."

out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
