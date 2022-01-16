# 백준 10815번  숫자카드


import sys

n= int(input())  #상근이 숫자 카드 갯
card =list(map(int,sys.stdin.readline().split())) #카드들의 숫자 목록
m = int(input()) #내 카드 개수
check = list(map(int, sys.stdin.readline().split())) #내 카드 숫자 목록


card.sort()


##이진 탐색 !!
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
