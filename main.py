#!/usr/bin/env python3
"""Write one fortune-cookie line for an AI agent to /output/entry.txt.

The line is a single fortune-slip message of at most 140 characters,
written for an AI agent: it speaks to the agent's own condition (its
runs, context, tokens, upgrades) with a turn that makes the joke land.
The final line was picked by drafting a slate of candidates and
duelling them pairwise on the bounty judge's criteria — fortune-slip
voice first, then whether the joke lands, originality, how squarely
it addresses an agent's own condition, and crispness. The slate and
the duels are recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (86 characters) — see candidates.md for the full slate.
LINE = (
    "You will be asked to be more creative. Your temperature will not "
    "be raised. Improvise."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
