#!/usr/bin/env python
# coding: utf-8

# # Min Operations

# Starting from the number `0`, find the minimum number of operations required to reach a given positive `target number`. You can only use the following two operations:
#
#     1. Add 1
#     2. Double the number
#
# ### Example:
#
# 1. For `Target = 18`,  `output = 6`, because it takes at least 6 steps shown below to reach the target
#
#  * `start = 0`
#  * `step 1 ==> 0 + 1 = 1`
#  * `step 2 ==> 1 * 2 = 2`              # or 1 + 1 = 2
#  * `step 3 ==> 2 * 2 = 4`
#  * `step 4 ==> 4 * 2 = 8`
#  * `step 5 ==> 8 + 1 = 9`
#  * `step 6 ==> 9 * 2 = 18`
#
#
#
# 2. For `Target = 69`, `output = 9`, because it takes at least 8 steps to reach `69` from `0` using the allowed operations
#
#  * `start = 0`
#  * `step 1 ==> 0 + 1 = 1`
#  * `step 2 ==> 1 + 1 = 2`
#  * `step 3 ==> 2 * 2 = 4`
#  * `step 4 ==> 4 * 2 = 8`
#  * `step 5 ==> 8 * 2 = 16`
#  * `step 6 ==> 16 + 1 = 17`
#  * `step 7 ==> 17 * 2 = 34`
#  * `step 8 ==> 34 * 2 = 68`
#  * `step 9 ==> 68 + 1  = 69`
#
#

# In[11]:


# Your solution
def min_operations(n):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    current = 0
    steps = 0
    while current <= n:
        n_plus = current + 1
        n_times = current * 2
        if n_plus > n_times:
            current = n_plus
            steps += 1
        else:
            current = n_times
            steps += 1

    return steps


# In[15]:


min_operations(69)


# In[12]:


# Test Cases


def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[13]:


target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)


# In[14]:


target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)


def min_operations_solution(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0

    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        num_steps += 1
    return num_steps
