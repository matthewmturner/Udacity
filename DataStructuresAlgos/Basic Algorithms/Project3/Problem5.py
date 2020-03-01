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
            if node.is_word:
                sufs.append(suffix)
                return
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


word_list = [
    "apple",
    "bear",
    "goo",
    "good",
    "goodbye",
    "goods",
    "goodwill",
    "gooses",
    "zebra",
]
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.insert(word)

# Test words
test_words = ["bear", "goo", "good", "goos"]
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))

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

word = MyTrie.find("t")
print(word.suffixes())
