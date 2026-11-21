import pytest

from calculator.calculator import add, subtract, multiply, divide, calculate


# ---------- Happy path ----------

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_calculate_add():
    assert calculate("add", 1, 1) == 2


# ---------- Sad path ----------

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_calculate_unknown_operation_returns_none():
    assert calculate("modulo", 5, 2) is None
