[//]: # (Links)
[Github-flavored markdown]: https://github.github.com/gfm

[manifest]: https://packaging.python.org/en/latest/guides/using-manifest-in
[packaging]: https://packaging.python.org/en/latest/tutorials/packaging-projects
[setup.cfg]: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html

[bump2version]: (https://github.com/c4urself/bump2version
[pre-commit]: https://pre-commit.com
[black]: https://github.com/psf/black

[pypi]: pypi.org
[test.pypi]: test.pypi.org

[Zenodo]: https://zenodo.org

[umsdk]: https://github.com/sensapex/umsdk
[sensapex-py]: https://github.com/sensapex/sensapex-py

[//]: # (Badges)
[//]: # ([![DOI]&#40;https://zenodo.org/badge/370470893.svg&#41;]&#40;https://zenodo.org/badge/latestdoi/370470893&#41;)
[//]: # ([![PyPI]&#40;https://img.shields.io/pypi/v/templatepy.svg&#41;]&#40;https://pypi.org/project/templatepy&#41;)
[//]: # ([![Wheel]&#40;https://img.shields.io/pypi/wheel/templatepy.svg&#41;]&#40;https://pypi.org/project/templatepy&#41;)
[//]: # (![CI]&#40;https://github.com/larsrollik/sensapex_api/workflows/tests/badge.svg&#41;)

[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/larsrollik/sensapex_api/blob/main/CONTRIBUTING.md)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fgithub.com/larsrollik/sensapex_api)](https://github.com/larsrollik/sensapex_api)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


# sensapex-api
Meta-API for Sensapex Manipulators from uMx family.
---

This is a meta-API for the Sensapex Python API, which is in turn a binding for the underlying C library.

## Functionality
- Set relative zero position for one or all axes
- Convenience methods to move signle axes (instead of giving vector for all axis, even if only intending to move one axis)

-> See `examples` folder for usage of the relative positioning on one or all axes.

## Install
1. Clone repo: `git clone https://github.com/larsrollik/sensapex-api.git`
2. Install package: `pip install sensapex-api`
3. Install sensapex UM SDK library
   1. Follow method in original repo: [umsdk] library
   2. or use version of `install_lib.sh` script (in this repo)

## Dependencies
- [sensapex-py] package that can be installed from [sensapex-py] or via `pip install sensapex`
- [umsdk] library
- numpy
- pyserial

## Contributing
Contributions are very welcome!
Please see the [contribution guidelines](https://github.com/larsrollik/templatepy/blob/main/CONTRIBUTING.md) or check out the [issues](https://github.com/larsrollik/templatepy/issues)

## License
This software is released under the **[BSD 3-Clause License](https://github.com/larsrollik/templatepy/blob/main/LICENSE)**.

This code is an abstraction layer on top of the MIT-licensed [sensapex-py] and the [umsdk].

---
**Version: "0.1.0"**
