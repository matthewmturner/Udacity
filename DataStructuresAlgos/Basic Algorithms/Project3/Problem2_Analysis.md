# Problem 2 Efficiency Analysis

Given that the input array is partially sorted (on an axis point) I figured I would still be able to use binary search but with some additional checks than what is required for traditional binary search.  The additional checks are to compare not only the mid element but also the start and end elements.  By adding these checks you can still complete the search in O(log(n)) time. Due to using a recursive approach to this problem the space complexity is O(n) since we keep the values of all the calls in memory until we reach the base case.
