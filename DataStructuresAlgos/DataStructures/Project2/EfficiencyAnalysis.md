# Project 2 Algorith Efficiency Analysis

## Problem 1: Least Recently Used Cache

I used a double linked list and dictionary as the core data structures to solve this problem.  These were chosen as they each have O(1) time for the uses I had (adding and removing from head or tail).  Each was chosen for the following reasons:

- **Double Linked List**: Tracks the usage of items accessing the cache.    The head is the most recently used and the tail the least recently used.
- **Dictionary**: Used as the cache to enable O(1) lookups.

While a linked list can have worst case O(n) complexity if you need to iterate through the entire list I only pulled from the head and tail which allowed for constant time lookups.

The space required for this is primarily composed of the dictionary used as the cache and the LinkedList nodes which each only get as large the cache size so are O(n) where n is the size of the cache.

## Problem 2: File Recursion

The time complexity for this is O(n) where n represents the number of files in a directory and all of its sub directories.

The space complexity for this is O(n) where n is the number of objects (files or directories) in the parent directory.  The call stack will grow each time there is an additional directory within a directory, so it can grow to m where m is the number of directories to be search.

## Problem 3: Huffman Encoding

The time complexity of this is O(n log(n)).  This comes from starting by iterating over the whole string to put the values into a dictionary to get there counts (n) and then using a priority queue which implements a heap under the hood that operates in (log n) time.

The space complexity is composed of the encoded data and the huffman tree to decode it as well as the priority queue for building the tree.

Because this uses a recursive function for each leaf node the call stack can grow to m where m is the depth of the tree.  

## Problem 4: Active Directory

In order to solve this I treated the problem similar to Problem 2 on File Recursion.  I wanted to traverse the parent(group), child(sub-group), attribute(user) relationships.  So in order to implement this I used a recursive solution again which results in O(n) complexity where n is the number of users in the group.

Because this uses a recursive function the call stack can grow to m where m is the number of groups in all groups and subgroups of the parent group.

## Problem 5: Blockchain

My approach for this was to have to distinct classes to create the blockchain.

- **Block**: A block was composed of a timestamp of the creation time, data, a hash, a reference to the previous blocks hash, and a reference to the next block in the chain.  The hash was generated with a calculate hash method of the class.
- **Blockchain**: The Blockchain class is composed of Block classes and is structured similar to a linked list where each block has a reference to the next and prior blocks with the class tracking the head and tail.  The two main functions are *add_block* which allows you to add a new block to the blockchain and *find_block_by_hash* which allows you to search for a block by it's hash.

The time complexity mainly comes from the calculation of the hash.  A LinkedList type structure was used (but calling the nodes Blocks instead) which allows for O(1) operation time separate from the computation of the hash.

The space complexity primarily comes from the amount of data to be stored in the block.  There is a fixed size amount from the date stamp and the hash but the data size will drive most of the Blocks size.

## Problem 6: Union and Intersection

For the *union* function which returns all elements from the two input linked lists I used a set which does not allow duplicate values as my result variable to hold all values from iterating through each linked list.  Since I had to iterate through each the complexity is O(n + m) where n is the length of llist_1 and m is the length of llist_2.

For the *intersection*, which only returns values in both linked lists, I needed to use two sets.  One to track the keys in the first linked list and the other to track the results.  Values were only added to the result during the loop through of the second linked list after it was checked whether the value was in the first.  Since I had to iterate through each the complexity is O(n + m) where n is the length of llist_1 and m is the length of llist_2.

The space complexity is also O(n + m) as they sizes of the linked lists will drive how much space is needed.
