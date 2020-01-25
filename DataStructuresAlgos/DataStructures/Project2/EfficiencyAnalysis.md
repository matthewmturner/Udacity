# Project 2 Algorith Efficiency Analysis

## Problem 1: Least Recently Used Cache
I used a double linked list and dictionary as the core data structures to solve this problem.  These were chosen as they each have O(1) time for the use I had.  Each was chosen for the following reasons:

- **Double Linked List**: Tracks the usage of items accessing the cache.    The head is the most recently used and the tail the least recently used.
- **Dictionary**: Used as the cache to enable O(1) lookups.

While a linked list can have worst case O(n) complexity if you need to iterate through the entire list I only pulled from the head and tail which allowed for constant time lookups. 