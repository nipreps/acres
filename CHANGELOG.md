# Changelog

<a id='changelog-0.4.1'></a>
## 0.4.1 — 2025-05-30

### Infrastructure

- Resolve issue with running tox from sdist.

<a id='changelog-0.4.0'></a>
## 0.4.0 — 2025-05-30

### Added

- An `acres.typ` module is added for providing access to the types
  accepted by or returned by `acres.Loader` and its methods.
  Use `acres.typ.Traversable` to annotate types without checking
  Python versions for its location.
  Use `from __future__ import annotations` to avoid unnecessary imports
  in Python 3.13 and lower.

- Documentation is now rendered at https://nipreps-acres.readthedocs.io

### Changed

- Increased type coverage of tests.

- The `importlib_resources` backport is no longer a dependency, even
  for older Python versions.

<a id='changelog-0.3.0'></a>
## 0.3.0 — 2025-02-22

### Changed

- Drop support for Python 3.8.

### Infrastructure

- Consolidate CI jobs to one per OS.

<a id='changelog-0.2.0'></a>
## 0.2.0 — 2024-12-09

This release changes the recommended usage and resolves issues with zip imports.

### Added

- Tests exercise and demonstrate the usage of acres on zipped modules.

### Changed

- Update recommended usage from `Loader(__package__)` to `Loader(__spec__.name)`.

### Fixed

- Resolve cache misses when caching the same file from different loaders.

<a id="changelog-0.1.1"></a>
## 0.1.1 — 2024-12-09

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
## 0.1.0 — 2024-07-16

Initial release of acres.
