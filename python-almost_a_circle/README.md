# Python - Almost a circle

An OOP project bringing together everything from the previous ones: inheritance,
encapsulation with private attributes and validated getters/setters, `*args`
and `**kwargs`, JSON and CSV serialization/deserialization, and a full
`unittest` suite.

## Requirements

- Interpreted on Ubuntu 20.04 LTS using `python3` (3.8.5)
- First line of every file is `#!/usr/bin/python3`
- pycodestyle (2.7.*) compliant; files end with a new line and are executable
- Every module, class and method has a real-sentence docstring

## Structure

```
models/
    __init__.py
    base.py         # Base: id management + JSON/CSV (de)serialization
    rectangle.py    # Rectangle(Base): validation, area, display, update
    square.py       # Square(Rectangle): size getter/setter, update
tests/
    test_models/
        test_base.py
        test_rectangle.py
        test_square.py
```

## Running the tests

```
python3 -m unittest discover tests
```

Or a single file:

```
python3 -m unittest tests/test_models/test_base.py
```
