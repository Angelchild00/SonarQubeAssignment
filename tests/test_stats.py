from calculator.calculator import calculate
from calculator.stats import average_of_list, mean_of_values, largest


# ---------- Happy path ----------

def test_average_of_list():
    assert average_of_list([1, 2, 3, 4]) == 2.5


def test_average_skips_none_values():
    assert average_of_list([2, None, 4]) == 3


def test_mean_matches_average():
    assert mean_of_values([1, 2, 3]) == average_of_list([1, 2, 3])


def test_largest():
    assert largest([3, 9, 2]) == 9


# ---------- Sad path ----------

def test_average_of_empty_list_is_zero():
    assert average_of_list([]) == 0


def test_average_of_none_is_zero():
    assert average_of_list(None) == 0


def test_largest_of_empty_list_returns_none():
    # Used to crash with IndexError: list index out of range
    assert largest([]) is None


def test_history_is_not_shared_between_calls():
    # Used to leak results between calls through a shared default list
    first = []
    calculate("add", 1, 1, first)
    second = []
    calculate("add", 2, 2, second)
    assert first == [2]
    assert second == [4]
    assert calculate.__defaults__ == (None,)
