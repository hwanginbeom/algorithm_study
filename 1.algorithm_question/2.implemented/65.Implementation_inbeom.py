import sys
import collections
import math

input = sys.stdin.readline
my_str = str(int(input()))

counter = collections.Counter(my_str).most_common()
answer = ''

def abc(counter):
    list_value=[]
    sum_96 = 0
    if len(counter) == 1:
        if counter[0][0] == '6' or counter[0][0] == '9':
            return math.ceil( int(counter[0][1])/2 )
        return counter[0][1]
    else:
        for i in counter:
            if i[0] == '6':
                sum_96 += int(i[1])
            if i[0] == '9':
                sum_96 += int(i[1])
            list_value.append(list(i))
        sum_96 = math.ceil(sum_96 / 2)
        for i in list_value:
            if i[0]=='9' or i[0]=='6':
                i[1] = sum_96
        max_value = 0
        for i in list_value:
            if i[1] > max_value:
                max_value = i[1]
        return max_value

print(abc(counter))