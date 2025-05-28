<!--
A new scriv changelog fragment.

Uncomment the section that is right (remove the HTML comment wrapper).
For top level release notes, leave all the headers commented out.
-->

### Added

- An `acres.typ` module is added for providing access to the types
  accepted by or returned by `acres.Loader` and its methods.
  Use `acres.typ.Traversable` to annotate types without checking
  Python versions for its location.
  Use `from __future__ import annotations` to avoid unnecessary imports
  in Python 3.13 and lower.

### Changed

- The `importlib_resources` backport is no longer a dependency, even
  for older Python versions.

<!--
### Fixed

- A bullet item for the Fixed category.

-->
<!--
### Deprecated

- A bullet item for the Deprecated category.

-->
<!--
### Removed

- A bullet item for the Removed category.

-->
<!--
### Security

- A bullet item for the Security category.

-->
<!--
### Infrastructure

- A bullet item for the Infrastructure category.

-->
