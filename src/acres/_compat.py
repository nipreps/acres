"""Compatibility module for importing the importlib.resources API.

There is a bug in 3.9 handling of zip modules on Windows, so keep this
around until the Python 3.9 end-of-life.
"""

import sys

if sys.version_info >= (3, 10):
    from importlib.resources import as_file, files
else:
    from importlib_resources import as_file, files


__all__ = ['files', 'as_file']
