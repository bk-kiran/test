# ANSWER KEY: for TLs only, don't share with students
import pytest
from calculator import add, subtract, multiply, divide


# SAMPLE TEST (given to students)
def test_add():
    assert add(2, 3) == 5          # normal case
    assert add(-2, -3) == -5       # negative numbers
    assert add(-4, 10) == 6        # mixed signs
    assert add(0, 0) == 0          # zero
    assert add(2.5, 0.5) == 3.0    # decimals


def test_subtract():
    assert subtract(5, 3) == 2         # normal case
    assert subtract(3, 5) == -2        # order matters (catches abs() bugs)
    assert subtract(-2, -3) == 1       # negatives
    assert subtract(7, 0) == 7         # zero
    assert subtract(2.5, 0.5) == 2.0   # decimals


def test_multiply():
    assert multiply(4, 3) == 12        # normal case
    assert multiply(-4, 3) == -12      # one negative
    assert multiply(-4, -3) == 12      # two negatives
    assert multiply(9, 0) == 0         # zero
    assert multiply(2.5, 2) == 5.0     # decimals


def test_divide():
    assert divide(10, 2) == 5          # even split
    assert divide(7, 2) == 3.5         # decimal answer (catches // bugs)
    assert divide(-9, 3) == -3         # negative
    assert divide(1, 4) == 0.25        # less than 1
    assert divide(1, 3) == pytest.approx(0.333, rel=1e-2)  # repeating decimal


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)