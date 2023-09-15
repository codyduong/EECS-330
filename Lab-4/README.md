# Lab 4 | EECS 330

While [ `poetry` ](https://python-poetry.org/) is used for dependency management, it works functionally the same as [ `conda` ](https://docs.conda.io/en/latest/)

## Pre-reqs

Read dependency file at [`pyproject.toml`](pyproject.toml) or see below:

* `python ^3.10.8`
  * Probably doesn't work on lower verisons, some type features are relatively new... Would require `__future__` for backporting
* `numpy ^1.25.2`
  * Probably works on lower versions if sem-ver is to be believed.

## Run

```sh
python main.py -v
```

or with Poetry (in pwsh)
```pwsh
poetry run python .\src -- -v
```

## Tests

Test cases are written using [ `unittest` ](https://docs.python.org/3/library/unittest.html) for testing. The tests can be found in [ `./tests` ](tests).

## Formatting
[`black`](https://github.com/psf/black) is used for formatting and code-styling.

```sh
black .
```

## Notes

* `Deque` and `DequeNP` are subclasses of `DLList` . It allows for `DLList` to either implement `Deque` or `DequeNP` for it's data handling. While class composition certainly would've been prettier here, didn't care to implement.

* Generic type implementation is weak specifically within `Deque`, `DequeNP`, and `DLList`. There is some issues with type invariances as well generic superclasses obsfucating type signatures, more work than it is worth to resolve.

* Many classes contain some magic methods to make working with them easier, ie. `__getitem__`, `__setitem__`, et. cetera
