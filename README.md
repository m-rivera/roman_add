# Roman Numeral Addition

## Overview

This program takes two Roman numerals as arguments and returns their sum as a
new Roman numeral.

## Compatibility

This program is tested and compatible with Python 2.7, and Python 3.0-3.6.
There are no external library requirements except for testing. Users intersted
in this should refer to the ['For Developers' section](#for-developers).

## Installation

When at the root of the project (`roman_add/`), run:

```bash
pip install .
```

And you're done!

## Use

The generic syntax is:

```bash
add_roman.py [-h] numeral_a numeral_b
```

So, for example:

```bash
add_roman.py IV V
```

Would return

```bash
add_roman.py IX
```

The input numbers need to be positive, in all capitals, and in the subtractive
Roman style (e.g. 4 is expressed as IV instead of IIII).
This information can be accessed with:

```bash
add_roman.py -h
```

## For Developers

The testing for this project uses [pytest](https://docs.pytest.org/en/latest/).
To run the tests, first install `pytest` if you haven't already:

```bash
pip install pytest
```

Then navigate to `roman_add/roman_add/tests/` and run:

```bash
pytest
```

This will run all unit tests in sequence, and finally functional tests.
