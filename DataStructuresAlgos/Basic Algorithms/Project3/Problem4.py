def sort_012(input_list):
    """
    Given an input array consisting of only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

    zeros = []
    ones = []
    twos = []

    sorted_list = []
    for n in input_list:
        if n == 0:
            zeros.append(0)
        elif n == 1:
            ones.append(1)
        elif n == 2:
            twos.append(2)
        else:
            raise ValueError("List must only have intgers of 0, 1, or 2")

    sorted_list = zeros + ones + twos

    return sorted_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Expected output: pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Expected output: pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Expected output: pass
test_function([1, 1, 1, 1, 1, 1, 1])
# Expected output: pass
test_function([1])
# Expected output: pass
test_function(120)
# Expected output: ValueError input must be a list
# Need to comment out above function to see error for below
test_function([1, 3])
# Expected output: ValueError List must only have integers of 0, 1, or 2
