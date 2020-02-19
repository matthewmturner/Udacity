def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    current_max = None
    current_min = None

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


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
