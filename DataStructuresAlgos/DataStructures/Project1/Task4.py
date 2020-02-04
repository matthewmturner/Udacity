"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_call_nums = set()
receiving_call_nums = set()
outgoing_text_nums = set()
receiving_text_nums = set()

for call in calls:
    outgoing_call_nums.add(call[0])
    receiving_call_nums.add(call[1])

for text in texts:
    outgoing_text_nums.add(text[0])
    receiving_text_nums.add(text[1])

possible_marketers = set()

for num in outgoing_call_nums:
    if (num not in receiving_call_nums) and (num not in outgoing_text_nums) and (num not in receiving_text_nums):
        possible_marketers.add(num)

print("These numbers could be telemarketers: ")
for num in sorted(possible_marketers):
    print(num)


