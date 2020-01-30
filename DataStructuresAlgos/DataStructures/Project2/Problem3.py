import sys
from collections import deque

class CharNode:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class Node:

    def __init__(self):
        self.freq = None
        self.left = None
        self.right = None

    def set_value():
        self.freq = self.left.freq + self.right.freq


def huffman_encoding(data):
    
    char_frequencies = {}

    for char in data:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    pairs = []
    for char, ct in char_frequencies.items():
        pair = (char, ct)
        pairs.append(pair)

    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    queue = deque()

    for char_pair in sorted_pairs:
        node = Node(char_pair[0], char_pair[1])
        queue.appendleft(node)

    while len(queue) > 1:
        node_smaller = queue.pop()
        node_small = queue.pop()
        node = Node()
        node.right = node_smaller
        node.left = node_small
        node.set_value()

    pass




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