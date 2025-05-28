from __future__ import annotations

import atexit
from contextlib import ExitStack
from functools import cache

import importlib.resources as res

from . import typ as t


EXIT_STACK = ExitStack()
atexit.register(EXIT_STACK.close)


@cache
def cached_resource(anchor: str | t.ModuleType, segments: tuple[str, ...]) -> t.Path:
    return EXIT_STACK.enter_context(res.as_file(res.files(anchor).joinpath(*segments)))
