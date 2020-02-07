import sys
from collections import deque, namedtuple
from queue import PriorityQueue

class CharNode:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.visited = False


class Node:

    # def __init__(self, left, right):
    #     self.char = None
    #     self.freq = None
    #     self.left = None
    #     self.right = None
    #     self.visited = False
        
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
    
    print(f"Characters in string: {len(data)}\n")
    char_frequencies = {}

    for char in data:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    pqueue = PriorityQueue()

    for char, ct in char_frequencies.items():
        node = Node()
        node.set_char_count(char, ct)
        pqueue.put((ct, node))
    
    while pqueue.qsize() > 1:
        node_smaller = pqueue.get()[1]
        node_small = pqueue.get()[1]
        node = Node()
        node.set_left(node_small)
        node.set_right(node_smaller)
        node.set_freq()
        pqueue.put((node.get_freq(), node))

    root_node = pqueue.get()[1]

    def pre_order(root):

        codes = {}

        def traverse(node, code, val):
            code += str(val)
            if node:
                if node.char:
                    codes[node.char] = code
                traverse(node.get_left(), code, 0)
                traverse(node.get_right(), code, 1)
        
        code = ""        
        traverse(root.get_left(), code, 0)        
        traverse(root.get_right(), code, 1)

        return codes

    codes = pre_order(root_node)

    for c, cd in codes.items():
        print(f"Char({c}): {cd}")
    print("")

    encoded_data = ""
    for char in data:
        encoded_data += codes[char]

    return encoded_data, root_node, codes

def huffman_decoding(data,tree):

    node = tree
    decoded_string = ""

    for char in data:
        if char == '0':
            node = node.get_left()
        elif char == '1':
            node = node.get_right()

        if node.char:
            decoded_string += node.char
            node = tree    

    return decoded_string


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree, codes = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))