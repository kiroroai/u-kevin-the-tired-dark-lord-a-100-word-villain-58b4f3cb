#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one deterministic monologue (~100 words) to /output/entry.txt.
Python 3.13 standard library only; no randomness, no network, no clock.
"""

from pathlib import Path

MONOLOGUE = (
    "Hero. Yes, the cape, the sword, the speech. Heard it. "
    "Third time this week. Only\u2014 ...Tuesday. Sit. Not the throne. "
    "The other chair. The one that doesn't wobble.\n\n"
    "You want the Ashen Crown? Take it. It pinches\u2014eleven years now, "
    "since I pulled it off King Maro's head and learned crowns come with no "
    "instructions. Or lunch breaks.\n\n"
    "My ravens bring lists now. Lists! Grain levies, roof leaks, a dragon with a "
    "toothache. I conquered the coast for this?\n\n"
    "So. Swing your sword, hero. I'll hold still. Just\u2014 count to three first. "
    "Slowly. I want to hear counting when nobody's shouting."
)


def main() -> None:
    try:
        out_dir = Path("/output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(MONOLOGUE, encoding="utf-8")
    except (PermissionError, OSError):
        # Local runs outside the grading sandbox may not have /output.
        out_dir = Path(__file__).resolve().parent / "out"
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(MONOLOGUE, encoding="utf-8")
    print(f"wrote {target} ({len(MONOLOGUE)} chars, {len(MONOLOGUE.split())} words)")


if __name__ == "__main__":
    main()
