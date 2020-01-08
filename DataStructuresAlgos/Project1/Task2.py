"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_times = {}

for record in calls:
    if record[0] not in call_times.keys():
        call_times[record[0]] = int(record[3])
    else:
        call_times[record[0]] += int(record[3])
    if record[1] not in call_times.keys():
        call_times[record[1]] = int(record[3])
    else:
        call_times[record[1]] += int(record[3])

max_call_time = 0
max_call_time_number = None

for number, time in call_times.items():
    if time > max_call_time:
        max_call_time = time
        max_call_time_number = number

print(f"{max_call_time_number} spent the longest time, {max_call_time} seconds, on the phone during September 2016.")