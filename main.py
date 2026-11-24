"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one funny, heartfelt sentence a robot says at its own wedding
to /output/entry.txt. Deterministic, standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def wedding_vow() -> str:
    """One sentence a robot speaks at its own wedding.

    Machine voice (simulations, patches, shutdown), a real laugh from
    the situation itself, and tenderness underneath: in a million
    futures, it still chooses this one person.
    """
    return (
        "I have run a million simulations of this day, and in every one "
        "I choose you \u2014 so I vow to keep choosing you, patch after "
        "patch, till my last shutdown."
    )


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(wedding_vow() + "\n")


if __name__ == "__main__":
    main()
