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
    
    print(f"Characters: {len(data)}")
    char_frequencies = {}

    for char in data:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1

    # pairs = []
    pqueue = PriorityQueue()
    # q = []
    for char, ct in char_frequencies.items():
        node = Node()
        node.set_char_count(char, ct)
        pqueue.put((ct, node))
        # q.append((ct, char))

    # q.sort(reverse=True)
    # for char_pair in sorted_pairs:
    #     # node = CharNode(char_pair.char, char_pair.count)
    #     node = Node()
    #     node.set_char_count(char_pair.char, char_pair.count)

    #     print(f"Node ({node.char}): {node.freq}")
    #     queue.appendleft(node)
    #     queue2.put((node, node.freq))

    while pqueue.qsize() > 1:
        # node_smaller = queue.pop()
        # node_small = queue.pop()
        node_smaller = pqueue.get()[1]
        node_small = pqueue.get()[1]
        # node_smaller3 = q.pop()
        # node_small3 = q.pop()
        # node = Node(node_small, node_smaller)
        # node3 = Node()
        # node3.set_left(node_small3)
        # node3.set_right(node_smaller3)
        # node3.set_freq()
        node = Node()
        node.set_left(node_small)
        node.set_right(node_smaller)
        node.set_freq()
        pqueue.put((node.get_freq(), node))
        # q.append((node.freq, node))
        # queue2.put(node2.freq, node2)

    root_node = pqueue.get()[1]

    # encoded_string = ""

    def pre_order(root):

        codes = {}

        def traverse(node, code):
            if node:
                if node.char:
                    codes[node.char] = code
                code += '0'
                traverse(node.get_left(), code)
                code += '1'
                traverse(node.get_right(), code)
        
        
        code = ""        
        traverse(root, code)

        return codes

    codes = pre_order(root_node)
    

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