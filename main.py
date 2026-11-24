#!/usr/bin/env python3
"""Fortune in a Pot entry: writes one kind, funny fortune for a houseplant to /output/entry.txt."""

import os

FORTUNE = "You will outgrow this pot, this windowsill, and every doubt your keeper ever had about their green thumb."

# The fortune is written for this plant in this window: the pot, the
# windowsill, and the keeper's green thumb. Specific, kind, and funny
# in the way a plant lover laughs, with the cadence of a prediction.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
