#!/usr/bin/env python3
"""A fancy Hello, World! — colors, typewriter effect, and a little flair."""

from __future__ import annotations

import argparse
import random
import sys
import time

# ANSI colors (works in most modern terminals)
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
COLORS = [
    "\033[91m",  # red
    "\033[93m",  # yellow
    "\033[92m",  # green
    "\033[96m",  # cyan
    "\033[94m",  # blue
    "\033[95m",  # magenta
]

BANNER = r"""
    ██╗  ██╗███████╗██╗     ██╗      ██████╗ 
    ██║  ██║██╔════╝██║     ██║     ██╔═══██╗
    ███████║█████╗  ██║     ██║     ██║   ██║
    ██╔══██║██╔══╝  ██║     ██║     ██║   ██║
    ██║  ██║███████╗███████╗███████╗╚██████╔╝
    ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
"""

SPARKLES = "✦ ✧ ★ ☆ · ˚ ✦"


def supports_color() -> bool:
    if not sys.stdout.isatty():
        return False
    if sys.platform == "win32":
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            return True
        except Exception:
            return False
    return True


def c(text: str, code: str, use_color: bool) -> str:
    if not use_color:
        return text
    return f"{code}{text}{RESET}"


def typewriter(text: str, delay: float = 0.04, use_color: bool = True) -> None:
    for i, ch in enumerate(text):
        color = COLORS[i % len(COLORS)] if use_color else ""
        sys.stdout.write(c(ch, color, use_color))
        sys.stdout.flush()
        time.sleep(delay * (0.3 if ch == " " else 1.0))
    print()


def rainbow_line(text: str, use_color: bool) -> None:
    if not use_color:
        print(text)
        return
    out = []
    for i, ch in enumerate(text):
        out.append(c(ch, COLORS[i % len(COLORS)], True))
    print("".join(out) + RESET)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fancy Hello, World!")
    parser.add_argument(
        "-n",
        "--name",
        default="World",
        help="Who to greet (default: World)",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Skip animations",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Plain text only",
    )
    args = parser.parse_args()

    use_color = supports_color() and not args.no_color
    delay = 0.0 if args.fast else 0.035

    print()
    rainbow_line(BANNER.strip("\n").split("\n")[0], use_color)  # top line accent
    if use_color:
        print(c(BANNER, DIM, True))
    else:
        print(BANNER)

    greeting = f"Hello, {args.name}!"
    print()
    print(c("  " + random.choice(SPARKLES.split()), COLORS[2], use_color), end=" ")
    if args.fast:
        rainbow_line(f"  {greeting}", use_color)
    else:
        sys.stdout.write("  ")
        typewriter(greeting, delay=delay, use_color=use_color)

    # decorative footer
    tagline = random.choice(
        [
            "Python says hi.",
            "May your bugs be shallow.",
            "print('magic')",
            "Have a brilliant day.",
        ]
    )
    print()
    print(c(f"  ── {tagline} ──", DIM, use_color))
    print(c(f"  {random.choice(SPARKLES.split())}  ", COLORS[4], use_color))
    print()


if __name__ == "__main__":
    main()
