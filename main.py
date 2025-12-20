def filter_even(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

print(filter_even([1, 2, 3, 4, 6]))

