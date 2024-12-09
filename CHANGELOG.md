
<a id='changelog-0.2.0'></a>
# 0.2.0 — 2024-12-09

This release changes the recommended usage and resolves issues with zip imports.

## Added

- Tests exercise and demonstrate the usage of acres on zipped modules.

## Changed

- Update recommended usage from `Loader(__package__)` to `Loader(__spec__.name)`.

## Fixed

- Resolve cache misses when caching the same file from different loaders.

<a id="changelog-0.1.1"></a>
# 0.1.1 — 2024-12-09

Bug-fix release in 0.1.x series.

Changed
-------

- Improved README to focus on usage patterns.
- Transitioned from flit to PDM for build backend.

 Fixed
 -----

 - Type annotations were expanded and verified against [mypy][] and [pyright][]
   across a range of Python versions.

[mypy]: https://www.mypy-lang.org/
[pyright]: https://microsoft.github.io/pyright

<a id="changelog-0.1.0"></a>
# 0.1.0 — 2024-07-16

Initial release of acres.
