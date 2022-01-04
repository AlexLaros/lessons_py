"""Closed-ended question methods.
--------------------------------------------------------------------------------
Currently available methods:
    - is_this_the_leap_year();
    - there_are_the_same_numbers();
    - there_are_the_same_neighbours().
--------------------------------------------------------------------------------
"""


def is_this_the_leap_year(year: int) -> str:
    """
    This function determines if the value of the year is a leap year.
    :param year: int
    :return: str
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Yes."
    else:
        return "No."


def there_are_the_same_numbers(num: int) -> str:
    """
    This function detects the presence of identical digits in a number.
    :param num: int
    :return: str
    """
    num_str = str(num)
    i = 0
    num = 0
    while i < len(num_str):
        count = num_str.count(num_str[i], 0, len(num_str))
        if count > 1:
            num = count
        i += 1

    if num > 1:
        return "Yes."
    else:
        return "No."


def there_are_the_same_neighbours(num: int) -> str:
    """
    This function detects the presence of identical neighboring digits
    in the number
    :param num: int
    :return: str
    """
    num_str = str(num)
    neighbor_count = 0
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            neighbor_count += 1

    if neighbor_count >= 1:
        return "Yes."
    else:
        return "No."


if __name__ == "__main__":
    pass
