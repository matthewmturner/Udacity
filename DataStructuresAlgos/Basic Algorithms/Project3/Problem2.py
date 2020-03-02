# Search in a Rotated Sorted Array
#
# You are given a sorted array which is rotated at some random pivot point.
#
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
#
# Example:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
#
# Here is some boilerplate code and test cases to start with:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    def recursive_rotated_array_search(array, target, start_idx, end_idx):

        if start_idx > end_idx:
            return -1

        start_element = array[start_idx]
        end_element = array[end_idx]

        mid_index = (start_idx + end_idx) // 2
        mid_element = array[mid_index]

        if mid_element == target:
            return mid_index
        elif ((target < mid_element) & (target >= start_element)) | (
            (target > mid_element) & (start_element > end_element)
        ):
            return recursive_rotated_array_search(
                array, target, start_idx, mid_index - 1
            )
        else:
            return recursive_rotated_array_search(array, target, mid_index + 1, end_idx)

    start = 0
    end = len(input_list) - 1

    number_idx = recursive_rotated_array_search(input_list, number, start, end)

    return number_idx


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Expected output: Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Expected output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Expected output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Expected output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Expected output: Pass
test_function([[4], 4])
# Expected output: Pass
test_function([[], 4])
# Expected output: Pass
