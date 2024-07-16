# Acres: Access resources on your terms

[![PyPI release](https://img.shields.io/pypi/v/acres.svg)](https://pypi.python.org/project/acres/)
[![Codecov Coverage report](https://codecov.io/github/nipreps/acres/graph/badge.svg?token=jVfxERJR5k)](https://codecov.io/github/nipreps/acres)

This module aims to provide a simple way to access package resources that will
fit most use cases.

The problem: `importlib.resources` provides a composable but ugly interface:

```python
from importlib.resources import files, as_file

with as_file(files(my_module) / 'data' / 'resource.ext') as resource_path:
    # Interact with resource_path as a pathlib.Path
```

The `files()` and `as_file()` functions do not make the meanings obvious,
and the different use cases do not obviously map on to these names.

The solution: `acres.Loader` is a class that provides read, filesystem
and cached filesystem access to package resources.

## Module data loader

Suppose you have a module structure:

```
src/
  mypkg/
    data/
      resourceDir/
        ...
      __init__.py
      resource.ext
    __init__.py
    ...
```

In `src/mypkg/data/__init__.py`, add:

```python
'''Data package

.. autofunction:: load_resource

.. automethod:: load_resource.readable

.. automethod:: load_resource.as_path

.. automethod:: load_resource.cached
'''

from acres import Loader

load_resource = Loader(__package__)
```

`mypkg.data.load_resource` is now a function that will return a `Path` to a
resource that is guaranteed to exist until interpreter exit:

```
from mypkg.data import load_resource

resource_file: Path = load_resource('resource.ext')
```

For additional control, you can use `load_resource.readable()` to return a `Path`-like
object that implements `.read_text()` and `.read_bytes()`:

```python
resource_contents: bytes = load_resource.readable('resource.ext').read_bytes()
```

Or a context manager with a limited lifetime:

```python
with load_resource.as_path('resourceDir') as resource_dir:
    # Work with the contents of `resource_dir` as a `Path`

# Outside the `with` block, `resource_dir` may no longer point to an existing path.
```

Note that `load_resource()` is a shorthand for `load_resource.cached()`,
whose explicitness might be more to your taste.

## On-demand data loading

`acres` may be used as a library to work with any package:

```python
from acres import Loader
import somepkg

text: str = Loader(somepkg).readable('data/someresource.txt').read_text()

with Loader(somepkg).as_path('data') as somepkgdata:
    walk_dir(somepkgdata)
```

If `Loader().cached()` is used, the resources will remain available until the
interpreter exists, even if the `Loader` instance is garbage collected.
