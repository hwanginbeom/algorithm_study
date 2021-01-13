# 2021-01-13

# https://www.acmicpc.net/problem/2750

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n=int(input())
array=[]

for _ in range(n):
    array.append(int(input()))


for i in range(len(array)):
    min_value=i
    for j in range(i+1,len(array)):
        if array[min_value]>array[j]:
            min_value=j
    array[i],array[min_value]=array[min_value],array[i]

for j in array:
    print(j,end='\n')

