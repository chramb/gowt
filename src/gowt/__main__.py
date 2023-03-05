from __future__ import annotations

import sys
from argparse import ArgumentParser, HelpFormatter
from typing import TYPE_CHECKING

from . import __version__

if TYPE_CHECKING:
    from argparse import Namespace
    from typing import Sequence


def main(args: Sequence[str] | None = None) -> int:
    argparser: ArgumentParser = ArgumentParser(prog="gowt", formatter_class=lambda prog: HelpFormatter(prog, max_help_position=35))
    argparser.add_argument("-V", "--version", action="version", version=f"{argparser.prog} {__version__}")
    argparser.add_argument("-r", "--repo", action="append", help="add repo location")
    argparser.add_argument("-c", "--config", action="append", help="add config location")
    parsed: Namespace = argparser.parse_args(args)
    _ = parsed
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
