## 10.sort_step4_statistic

# from collections import Counter
import sys
input = sys.stdin.readline

num = int(input())
array = []

for i in range(num):
    array.append(int(input()))

def statistic(input_list):
    sum = 0
    mean = 0
    median = 0
    mode = 0

    scope = max(input_list)-min(input_list)
    middle_index = (len(input_list)//2)

    sorted_list = sorted(input_list)

    for idx, item in enumerate(sorted_list):
        sum += item
        if idx == middle_index:
            median = item

    mean = round(sum/len(input_list))

    dic = {}
    for i in input_list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    result = [a for a, b in dic.items() if b == max(sorted(dic.values()))]

    if len(result) == 1:
        mode = result[0]
    else:
        mode = result[1]



    print(mean)
    print(median)
    print(mode)
    print(scope)

statistic(array)


## 11.sort_step5_SortInside

array = list(map(int, list(input())))
array.sort(reverse=True)
for i in range(len(array)) :
    print(array[i], end = "")