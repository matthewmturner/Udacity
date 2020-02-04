import sys
from collections import deque, namedtuple

class CharNode:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


class Node:

    def __init__(self, left, right):
        self.freq = None
        self.left = left
        self.right = right

    def set_freq(self):
        self.freq = self.left.freq + self.right.freq


def huffman_encoding(data):
    
    char_frequencies = {}

    for char in data:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    pairs = []
    for char, ct in char_frequencies.items():
        CharCount = namedtuple('Pair', ['char', 'count'])
        pair = CharCount(char=char, count=ct)
        pairs.append(pair)

    sorted_pairs = sorted(pairs, key=lambda x: x.count)
    queue = deque()

    for char_pair in sorted_pairs:
        node = CharNode(char_pair.char, char_pair.count)
        queue.appendleft(node)

    while len(queue) > 1:
        node_smaller = queue.pop()
        node_small = queue.pop()
        node = Node(node_small, node_smaller)
        node.set_freq()
        queue.appendleft(node)

    root_node = queue.pop()

    encoded_string = ""

    def tree_traverse(char):
        node = root_node
        char_code = ''
        if node.left == char:
            char_code += 0
            return char_code
        elif node.right == char:
            char_code += 1
            return char_code
        else:
            node = 
            


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))