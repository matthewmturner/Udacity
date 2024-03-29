import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    current_max = None
    current_min = None

    if (len(ints) == 0) or (ints is None):
        return tuple([current_min, current_max])

    for i, n in enumerate(ints):
        if i == 0:
            current_max = n
            current_min = n
        else:
            if n > current_max:
                current_max = n
            elif n < current_min:
                current_min = n

    return tuple([current_min, current_max])


list1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(list1)
list2 = [i for i in range(50, 100)]
random.shuffle(list2)

print("Pass" if ((0, 9) == get_min_max(list1)) else "Fail")
print("Pass" if ((50, 99) == get_min_max(list2)) else "Fail")
print("Pass" if (0, 0) == get_min_max([0]) else "Fail")
print("Pass" if (None, None) == get_min_max([]) else "Fail")
