# Lab 10 | EECS 330

While [ `poetry` ](https://python-poetry.org/) is used for dependency management, it works functionally the same as [ `conda` ](https://docs.conda.io/en/latest/)

## Pre-reqs

Read dependency file at [`pyproject.toml`](pyproject.toml) or see below:

* `python 3.10.8`
  * Probably doesn't work on lower verisons, some type features are relatively new... Would require `__future__` for backporting

## Run

```sh
python main.py
```

or with Poetry (in pwsh)
```pwsh
poetry run python .\main.py
```

## Tests

Test cases are written using [ `unittest` ](https://docs.python.org/3/library/unittest.html) for testing. The tests can be found in [ `./tests` ](tests).

```sh
python -m unittest -v tests.tests
```

## Formatting
[`black`](https://github.com/psf/black) is used for formatting and code-styling.

```sh
black .
```

