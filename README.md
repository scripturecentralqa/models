# Models

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Overview

Models and code to process data for [I Love Conference](https://iloveconference.org).

Can be repurposed to create models and process data for any semantic search project.

## Requirements

- python 3.10
- Poetry: `curl -sSL https://install.python-poetry.org | python3 - --version 1.4.0`
- nox: `pipx install nox && pipx inject nox nox-poetry`

## Installation

`poetry install`

## Downloading data

`mkdir data`

`aws s3 sync s3://iloveconference.data data`

## Running notebooks

`` env PYTHONPATH=`pwd` jupyter notebook ``

or (if you have fish shell)

`env PYTHONPATH=(pwd) jupyter notebook`

## Running Label Studio

`docker run -it -p 8080:8080 -v ~/iloveconference/labelstudio-data:/label-studio/data heartexlabs/label-studio:latest`

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Models_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/iloveconference/models/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/iloveconference/models/blob/main/LICENSE
[contributor guide]: https://github.com/iloveconference/models/blob/main/CONTRIBUTING.md
