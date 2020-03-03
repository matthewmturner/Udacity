class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """Take all unique elements from each linked list and add them to set.
    Arguments:
        llist_1 {LinkedList} -- LinkedList 1 containing data
        llist_2 {LinkedList} -- LinkedList 2 containing data
    Returns:
        [set] -- Set of all unique items from combined list
    """
    if (not isinstance(llist_1, LinkedList)) or (not isinstance(llist_2, LinkedList)):
        raise ValueError("Inputs must be LinkedList objects")

    result = set()

    node_1 = llist_1.head
    while node_1:
        result.add(node_1.value)
        node_1 = node_1.next

    node_2 = llist_2.head
    while node_2:
        result.add(node_2.value)
        node_2 = node_2.next

    return result


def intersection(llist_1, llist_2):
    """Finds elements that are in both linked lists and returns them in a set.
    Arguments:
        llist_1 {LinkedList} -- LinkedList 1 containing data
        llist_2 {LinkedList} -- LinkedList 2 containing data
    Returns:
        [set] -- Set of items that were in each LinkedList
    """

    if (not isinstance(llist_1, LinkedList)) or (not isinstance(llist_2, LinkedList)):
        raise ValueError("Inputs must be LinkedList objects")

    keys = set()
    result = set()

    node_1 = llist_1.head
    while node_1:
        keys.add(node_1.value)
        node_1 = node_1.next

    node_2 = llist_2.head
    while node_2:
        if node_2.value in keys:
            result.add(node_2.value)
        node_2 = node_2.next

    return result


if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    # Expected output: {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}
    print(intersection(linked_list_1, linked_list_2))
    # Expected output: {4, 21, 6}

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    # Expected output: {65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23}
    print(intersection(linked_list_3, linked_list_4))
    # Expected output: Empty set

    # Test case 3
    print(union(5, 6))
    # Expected output: ValueError for wrong input types
