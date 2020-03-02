# Problem 5 Efficiency Analysis

Word tries have time complexity of O(n) where n is the number of characters in the word and space complexity of O(m) where m is the number of characters in all of the words in the trie combined.  In order to find the suffixes of a given prefix we use a recursive solution.  This will have time and space complexity of O(n) where n is the number of characters in all of the suffixes.  We needed to use a recursive approach given that we did not know how many suffixes there were or how many characters in each.
