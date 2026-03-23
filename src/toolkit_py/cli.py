"""CLI entrypoint for toolkit_py."""

from __future__ import annotations

import argparse
from pathlib import Path

from .files import list_files
from .strings import camel_case, kebab_case, slugify, snake_case


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="toolkit-py", description="Small Python utility toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    slug_parser = subparsers.add_parser("slugify", help="Convert text into different naming formats")
    slug_parser.add_argument("text", help="Input text")
    slug_parser.add_argument(
        "--style",
        choices=["slug", "snake", "kebab", "camel"],
        default="slug",
        help="Output style",
    )

    tree_parser = subparsers.add_parser("tree", help="List files under a directory")
    tree_parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    tree_parser.add_argument("--pattern", default="*", help="Glob pattern to match")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "slugify":
        formatters = {
            "slug": slugify,
            "snake": snake_case,
            "kebab": kebab_case,
            "camel": camel_case,
        }
        print(formatters[args.style](args.text))
        return

    if args.command == "tree":
        root = Path(args.path).resolve()
        for file_path in list_files(root, args.pattern):
            print(file_path.relative_to(root))
        return

    parser.error("Unknown command")


if __name__ == "__main__":
    main()
