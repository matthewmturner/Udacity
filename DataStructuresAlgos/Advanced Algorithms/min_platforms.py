#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement
#
# Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.
#
# You will be given arrival and departure times in the form of a list.
#
# Note: Time `hh:mm` would be written as integer `hhmm` for e.g. `9:30` would be written as `930`. Similarly, `13:45` would be given as `1345`

# In[25]:


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """

    trains = len(arrival)
    platforms = 0
    for i in range(trains):
        if i == 0:
            platforms += 1
        elif arrival[i] < departure[i - 1]:
            platforms += 1

    return platforms


# In[26]:


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
min_platforms(arrival, departure)


# <span class="graffiti-highlight graffiti-id_khuho24-id_mgzo0p4"><i></i><button>Hide Solution</button></span>

# In[ ]:


def min_platforms_solution(arrival, departure):
    arrival.sort()
    departure.sort()

    platform_count = 1
    output = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):

        if arrival[i] < departure[j]:
            platform_count += 1
            i += 1

            if platform_count > output:
                output = platform_count
        else:
            platform_count -= 1
            j += 1

    return output


# In[3]:


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[6]:


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)


# In[ ]:


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
