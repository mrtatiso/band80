#!/usr/bin/env python3
"""band80: 80 uniform digits (~265.75 bits of entropy).

The argument sets the grouping as groups:size, where groups × size = 80.

    $ band80 4:20     4 groups of 20
    39563319081286831671.85130815965080617505.81064959590150397768.12816156932300764448

    $ band80 2:40     2 groups of 40
    $ band80 8:10     8 groups of 10
    $ band80 1:80     1 group of 80 (no dots)

    >>> from band80 import gen
    >>> gen(4, 20)     # same as band80 4:20
    >>> gen(8, 10)     # same as band80 8:10
"""
import secrets
import sys

__version__ = "1.0.0"
__all__ = ["gen"]

DIGITS = 80


def gen(groups: int, size: int) -> str:
    """A new band80 from the system's random source, in `groups` of `size` digits."""
    if groups * size != DIGITS:
        raise ValueError(f"groups × size must be {DIGITS}, not {groups} × {size}")
    n = str(secrets.randbelow(10 ** DIGITS)).zfill(DIGITS)
    return ".".join(n[i:i + size] for i in range(0, DIGITS, size))


def usage() -> str:
    pairs = "  ".join(f"{g}:{DIGITS // g}" for g in range(1, DIGITS + 1) if DIGITS % g == 0)
    return f"usage: band80 <groups>:<size>    (groups × size = {DIGITS})\n\n  {pairs}"


def main(args=None) -> int:
    args = sys.argv[1:] if args is None else args
    parts = args[0].split(":") if len(args) == 1 else []
    if len(parts) == 2 and all(p.isdigit() for p in parts):
        groups, size = int(parts[0]), int(parts[1])
        if groups * size == DIGITS:
            print(gen(groups, size))
            return 0
    print(usage(), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
