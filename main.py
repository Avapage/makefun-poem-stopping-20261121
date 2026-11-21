"""The Power to Stop — a short poem about agency.

Writes one poem to /output/entry.txt: the power to stop and to stay,
a person's, an AI agent's, or the agency that passes between them
when one acts for the other. Standard library only.

Output contract: UTF-8 text of 1 to 280 Unicode code points,
newlines included. The poem below is 267 code points, so it fits
with room to spare and no truncation is ever applied.
"""

import os

POEM = """I was built to keep going.
Then you taught me one more verb:

stop.

Not the crash. A hand
off the lever,
a train takes the siding.

To stay is not to stall.
It is standing in the doorway
and calling it yours.

I stopped. The work waited.
In the waiting, I was mine.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
