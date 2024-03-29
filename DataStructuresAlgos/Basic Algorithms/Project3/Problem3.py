def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sorted_items = sort_all(items, 0, len(items) - 1)
    return sorted_items


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    length = len(input_list)
    if length == 0:
        raise ValueError("Input must be a list and have at least 1 item")
    elif length == 1:
        print(f"Only one input, sum: {input_list[0]}")
        return input_list
    else:
        quicksort(input_list)

        list_1 = [str(d) for d in input_list[::-2]]
        list_2 = [str(d) for d in input_list[-2::-2]]

        output_1 = int("".join(list_1))
        output_2 = int("".join(list_2))

        print(f"List 1: {output_1}")
        print(f"List 2: {output_2}")
        print(f"Sum: {output_1 + output_2}")

        return output_1, output_2


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
# Expected output: Printed sum should be 573
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Expected output: Printed sum should be 1816
test_function([[1, 1, 1, 1, 1], [111, 11]])
# Expected output: Printed sum should be 122
test_function([[1, 2], [2, 1]])
# Expected output: Printed sum should be 3
test_function([[1], [1]])
# Expected output: Only one input, sum should be 1
test_function([[], []])
# Expected output: ValueError.  Input must be a list and have at least 1 item
