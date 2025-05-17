#!/usr/bin/env python3
"""
quickstart.py – minimal, production-grade skeleton.

Why it exists
-------------
* Gives you argparse, logging, and a tiny bit of business logic in <50 LOC.
* Provides one obvious place (`greet()`) to swap in real work later.
"""

import argparse
import logging
import os
from datetime import datetime


# ─── Configurable logging (respects $LOGLEVEL env var) ─────────────────────────
logging.basicConfig(
    level=os.getenv("LOGLEVEL", "INFO"),
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def greet(name: str) -> str:
    """Return a timestamped greeting (placeholder for real work)."""
    timestamp = datetime.now().strftime("%H:%M")
    return f"Hello, {name}! It is {timestamp}."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quickstart CLI template.")
    parser.add_argument(
        "--name",
        default="World",
        help="Who to greet (defaults to 'World').",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.info(greet(args.name))


if __name__ == "__main__":
    main()
