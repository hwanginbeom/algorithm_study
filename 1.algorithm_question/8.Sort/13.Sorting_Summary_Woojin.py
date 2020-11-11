### 로프

import sys
n = int(sys.stdin.readline())

rope_list = list()

max_weight = 0

for i in range(n):
    x = int(sys.stdin.readline())
    rope_list.append(x)

rope_list.sort(reverse=True)

for i in range(len(rope_list)):
    if max_weight < (rope_list[i]*(i+1)) :
        max_weight = (rope_list[i]*(i+1))
    else:
        continue

print(max_weight)


### 회의실 배정

import sys


def counting(meeting):
    meeting_count = 0
    start_time = 0

    for time in meeting:
        if time[0] >= start_time:
            start_time = time[1]
            meeting_count += 1
    return meeting_count

mCount = int(sys.stdin.readline())
time_table = []

for i in range(mCount):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append((start, end))

time_table = sorted(time_table, key=lambda time: (time[1], time[0]))

print(counting(time_table))
