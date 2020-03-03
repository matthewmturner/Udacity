import sys
from queue import PriorityQueue


class Node:
    def __init__(self):
        self.char = None
        self.freq = None
        self.left = None
        self.right = None
        self.visited = False

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_char_count(self, char, freq):
        self.char = char
        self.freq = freq

    def set_freq(self):
        self.freq = self.left.get_freq() + self.right.get_freq()

    def get_freq(self):
        return self.freq

    def visit(self):
        self.visited = True

    def __eq__(self, other):
        return self.get_freq() == other.get_freq()

    def __lt__(self, other):
        return self.get_freq() < other.get_freq()


def huffman_encoding(data):
    """Takes a string and compresses it using a huffman encoding approach.
    Arguments:
        data {str} -- String to be encoded
    Returns:
        [str, Node, dict] -- Encoded string, accompanying tree to decode, and codes for each letter
    """

    print(f"Characters in string: {len(data)}\n")
    if len(data) == 0:
        return "0", None, None

    char_frequencies = {}

    for char in data:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    pqueue = PriorityQueue()

    for char, ct in char_frequencies.items():
        node = Node()
        node.set_char_count(char, ct)
        pqueue.put((ct, node))

    if pqueue.qsize() == 1:
        root_node = Node()
        leaf_node = pqueue.get()[1]
        root_node.set_left(leaf_node)
    else:
        while pqueue.qsize() > 1:
            node_smaller = pqueue.get()[1]
            node_small = pqueue.get()[1]
            node = Node()
            node.set_left(node_small)
            node.set_right(node_smaller)
            node.set_freq()
            pqueue.put((node.get_freq(), node))

        root_node = pqueue.get()[1]

    def traverse(root):

        codes = {}

        def recursive_traverse(node, code, val):
            code += str(val)
            if node:
                if node.char:
                    codes[node.char] = code
                recursive_traverse(node.get_left(), code, 0)
                recursive_traverse(node.get_right(), code, 1)

        code = ""
        recursive_traverse(root.get_left(), code, 0)
        recursive_traverse(root.get_right(), code, 1)

        return codes

    codes = traverse(root_node)

    for c, cd in codes.items():
        print(f"Char({c}): {cd}")
    print("")

    encoded_data = ""
    for char in data:
        encoded_data += codes[char]

    return encoded_data, root_node, codes


def huffman_decoding(data, tree):
    """Takes encoded data and the accompanying huffman tree to decode the data
    Arguments:
        data {str} -- String of 1s and 0s representing encoded data
        tree {Node} -- Root node to decode the data
    Returns:
        [str] -- Decoded string that should match original encoded data
    """

    if tree is None:
        return ""

    node = tree
    decoded_string = ""

    for char in data:
        if char == "0":
            node = node.get_left()
        elif char == "1":
            node = node.get_right()

        if node.char:
            decoded_string += node.char
            node = tree

    return decoded_string


if __name__ == "__main__":

    ##### Test 1 #####
    a_great_sentence = "The bird is the word"

    print("Size of data: {}".format(sys.getsizeof(a_great_sentence)))
    print("Content of data: {}".format(a_great_sentence))

    encoded_data, tree, codes = huffman_encoding(a_great_sentence)

    print("Size of encoded data: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("Content of encoded data: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Size of decoded data: {}".format(sys.getsizeof(decoded_data)))
    print("Content of encoded data: {}\n".format(decoded_data))

    ##### Test 2 #####
    the_great_sentence = "The"

    print("Size of data: {}".format(sys.getsizeof(the_great_sentence)))
    print("Content of data: {}".format(the_great_sentence))

    encoded_data, tree, codes = huffman_encoding(the_great_sentence)

    print("Size of encoded data: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("Content of encoded data: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Size of decoded data: {}".format(sys.getsizeof(decoded_data)))
    print("Content of encoded data: {}\n".format(decoded_data))

    ##### Test 3 #####
    blank_great_sentence = ""

    print("Size of data: {}".format(sys.getsizeof(blank_great_sentence)))
    print("Content of data: {}".format(blank_great_sentence))

    encoded_data, tree, codes = huffman_encoding(blank_great_sentence)

    print("Size of encoded data: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("Content of encoded data: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Size of decoded data: {}".format(sys.getsizeof(decoded_data)))
    print("Content of encoded data: {}\n".format(decoded_data))

    ##### Test 4 #####
    blank_great_sentence = "AAAAA"

    print("Size of data: {}".format(sys.getsizeof(blank_great_sentence)))
    print("Content of data: {}".format(blank_great_sentence))

    encoded_data, tree, codes = huffman_encoding(blank_great_sentence)

    print("Size of encoded data: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("Content of encoded data: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("Size of decoded data: {}".format(sys.getsizeof(decoded_data)))
    print("Content of encoded data: {}\n".format(decoded_data))
