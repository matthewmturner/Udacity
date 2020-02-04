# Runtime Analysis

Task0: O(1)
Constant run time for each print as I am directly accessing the attribute I need without iteration.

Task1: O(n)
Linear run time for each as it is a simple iteration through each list

Task2: O(n)
Approximately 2N as we first loop through the raw list and then loop through a subset of the raw list.

Task3: O(n log n)
Approximately 2N as I loop through the data once and apply logic and then loop through again 
to print sorted and one per line. Additionally there is the overhead of using sorted which in python uses timsort 
which has O (n log n) complexity.

Task4: O (n log n)
Approximately as I have to loop through all calls, all texts, then a comparison of the 
extracted data sets and then printing a sorted and one per line view. Additionally there is the overhead 
of using sorted which in python uses timsort which has O (n log n) complexity.