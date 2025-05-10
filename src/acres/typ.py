# Copyright The NiPreps Developers <nipreps@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
#
# This module was inspired by async_utils._typings:
# https://github.com/mikeshardmind/async-utils/blob/7bf094f/src/async_utils/_typings.py
#
# This module was also licensed as Apache 2.
"""Typing symbols for the acres package.

This module aims to make the types used by the acres package available
for type checking without requiring the original packages to be imported
at runtime.

The expected usage is::

    import acres.typ as at

    def resource_using_function(resource: at.Traversable) -> ReturnType:
        ...

To get the runtime benefits of using this module, you should not import
anything from it, but import the module and access symbols as attributes.

The primary use for this in downstream tools is the
:class:`~importlib.resources.abc.Traversable` type, which will be imported
from ``importlib.resources`` or ``importlib_resources``, based on the Python
version. However, other types that are not directly used in acres are also
available.
"""
import sys

TYPE_CHECKING = False
if TYPE_CHECKING:
    from contextlib import AbstractContextManager
    from pathlib import Path
    from types import ModuleType

    if sys.version_info >= (3, 11):
        from importlib.resources.abc import Traversable
    else:
        from importlib_resources.abc import Traversable
else:

    def __getattr__(name: str) -> object:
        types = {
            'AbstractContextManager': 'contextlib',
            'Path': 'pathlib',
            'ModuleType': 'types',
            'Traversable': 'importlib.resources.abc'
            if sys.version_info >= (3, 11)
            else 'importlib_resources.abc',
        }
        try:
            return getattr(__import__(types[name]), name)
        except KeyError:
            raise AttributeError(f'module {__name__!r} has no attribute {name!r}')


__all__ = (
    'TYPE_CHECKING',
    'AbstractContextManager',
    'ModuleType',
    'Path',
    'Traversable',
)
