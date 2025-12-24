def filter_even(numbers: list[int]) -> list[int]:
    """
    Return a list of even numbers from the input list.
    """
    # TODO: implement
    pass






def filter_even(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def test_mixed_numbers():
    assert filter_even([1, 2, 3, 4, 6]) == [2, 4, 6]


def test_no_even_numbers():
    assert filter_even([1, 3, 5]) == []


def test_empty_list():
    assert filter_even([]) == []


def test_includes_zero():
    assert filter_even([0, 1, 2]) == [0, 2]


def test_negative_numbers():
    assert filter_even([-4, -3, -2, -1]) == [-4, -2]


print(filter_even([1, 2, 3, 4, 6]))