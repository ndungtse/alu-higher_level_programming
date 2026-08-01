# Python - Test-driven development

Small, well-documented functions built test-first, with interactive doctests
(in `tests/*.txt`) and a `unittest` suite for `max_integer`.

## Requirements

- Interpreted on Ubuntu 20.04 LTS using `python3` (3.8.5)
- First line of every file is `#!/usr/bin/python3`
- pycodestyle (2.7.*) compliant; all files end with a new line and are executable
- Every module and function has a real-sentence docstring

## Running the tests

Doctests (text files in `tests/`):

```
python3 -m doctest ./tests/*.txt
```

Unittest for `max_integer`:

```
python3 -m unittest tests.6-max_integer_test
```

## Tasks

| File | Test | Description |
|------|------|-------------|
| `0-add_integer.py` | `tests/0-add_integer.txt` | Add two integers/floats |
| `2-matrix_divided.py` | `tests/2-matrix_divided.txt` | Divide a matrix by a number |
| `3-say_my_name.py` | `tests/3-say_my_name.txt` | Print a full name |
| `4-print_square.py` | `tests/4-print_square.txt` | Print a `#` square |
| `5-text_indentation.py` | `tests/5-text_indentation.txt` | Break text after `.`, `?`, `:` |
| `6-max_integer.py` | `tests/6-max_integer_test.py` | Max of a list (unittest) |
| `100-matrix_mul.py` | `tests/100-matrix_mul.txt` | Multiply two matrices (advanced) |
| `101-lazy_matrix_mul.py` | `tests/101-lazy_matrix_mul.txt` | Multiply matrices with NumPy (advanced) |
