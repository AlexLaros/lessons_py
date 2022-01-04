"""Different sequence sorting methods.
--------------------------------------------------------------------------------
Currently available sequence sorting methods:
    - bubble();
    - choice();
    - insert();
    - quick().
--------------------------------------------------------------------------------
"""
__all__ = ['bubble', 'choice', 'insert', 'quick']


def bubble(lis):
    """
    This is the ''bubble'' sort function.
    :return: lis
    """
    n = len(lis)
    for i in range(n - 1):
        for j in range(n - 2, i - 1, -1):
            if lis[j + 1] < lis[j]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def choice(lis):
    """
    This is the sort function by selection.
    :return: lis
    """

    n = len(lis)

    for i in range(n - 1):
        n_min = i
        for j in range(i + 1, n):
            if lis[j] < lis[n_min]:
                n_min = j
        if i != n_min:
            lis[i], lis[n_min] = lis[n_min], lis[i]

    return lis


def insert(lis):
    """
    This is the insertion sort function.
    :return: lis
    """

    for i in range(1, len(lis)):
        item_to_insert = lis[i]
        j = i - 1

        while j >= 0 and lis[j] > item_to_insert:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = item_to_insert

    return lis


# additional function for "quick" sort function
def _partition(lis, low, high):
    pivot = lis[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while lis[i] < pivot:
            i += 1
        j -= 1
        while lis[j] > pivot:
            j -= 1
        if i >= j:
            return j

        lis[i], lis[j] = lis[j], lis[i]


def quick(lis):
    """
    This is a "quick" sort function
    :return: lis
    """

    def _quick(items, low, high):
        if low < high:
            split_index = _partition(items, low, high)
            _quick(items, low, split_index)
            _quick(items, split_index + 1, high)

    _quick(lis, 0, len(lis) - 1)
    return lis


if __name__ == "__main__":
    lst = [6, 13, 1, 12, 76]
    print(bubble(lst))
    print(choice(lst))
    print(insert(lst))
    print(quick(lst))
