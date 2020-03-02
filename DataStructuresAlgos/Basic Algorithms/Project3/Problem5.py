## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix=""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        sufs = []

        def recursive_suffixes(node, suffix=""):
            if (node.is_word) and (node.children is None):
                sufs.append(suffix)
                return
            elif (node.is_word) and (node.children is not None):
                sufs.append(suffix)
            word = suffix
            for char, node in node.children.items():
                word += char
                recursive_suffixes(node, word)
                word = word[:-1]

        for char, node in self.children.items():
            recursive_suffixes(node, suffix=char)

        return sufs


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for char in word:
            if char not in current.children.keys():
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return current

    def exists(self, word):
        string = self.find(word)
        return string.is_word


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)

t = MyTrie.find("t")
print(t.suffixes())
# Expected output: ['rie', 'rigger', 'rigonometry', 'ripod']
t = MyTrie.find("trig")
print(t.suffixes())
# Expected output: ['ger', 'onometry']
f = MyTrie.find("f")
print(f.suffixes())
# Expected output: ['un', 'unction', 'actory']
a = MyTrie.find("a")
print(a.suffixes())
# Expected output: ['nt', 'nthology', 'ntagonist', 'ntonym']
z = MyTrie.find("z")
print(z)
# Expected result: False
print(z.suffixes())
# Expevted result: AttributeError bool object has no attribute suffixes
