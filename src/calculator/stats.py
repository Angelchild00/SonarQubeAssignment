"""Basic statistics helpers."""


def average_of_list(numbers):
    if numbers is None:
        return 0
    total = 0
    count = 0
    for number in numbers:
        if number is None:
            continue
        total = total + number
        count = count + 1
    if count == 0:
        return 0
    average = total / count
    return round(average, 2)


def mean_of_values(values):
    """Kept for backwards compatibility; same as average_of_list."""
    return average_of_list(values)


def largest(numbers):
    """Return the largest number, or None for an empty or missing list."""
    if not numbers:
        return None
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest
