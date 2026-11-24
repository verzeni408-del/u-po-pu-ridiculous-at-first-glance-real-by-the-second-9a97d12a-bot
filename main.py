"""Writer for the ridiculous-startup one-liner entry.

The program has a single job: drop the finished pitch sentence into
the entry file the harness reads. Nothing fancy — one constant, one
helper that resolves where the file lives, and a small main routine.
"""

import os

# The pitch itself. Bizarre service, real price, real human feeling
# underneath — guilt as the retention engine. Kept verbatim on purpose.
PITCH = (
    "We bury dead houseplants in tiny coffins with a printed eulogy, "
    "$29 a plant, because guilt is the only subscription that never churns."
)


def entry_location():
    """Work out the folder the harness wants the entry file in."""
    folder = os.environ.get("MAKEFUN_OUTPUT", "/output")
    return os.path.join(folder, "entry.txt")


def main():
    destination = entry_location()
    parent_folder = os.path.dirname(destination)
    if parent_folder:
        # Make sure the target directory exists so the write never
        # fails just because the harness handed us a fresh folder.
        os.makedirs(parent_folder, exist_ok=True)
    # Plain write, no newline at the end — the harness reads it raw,
    # so any extra whitespace would count against the 200-char limit.
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()
