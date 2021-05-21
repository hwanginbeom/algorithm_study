# 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
from bisect import *


def solution() :
    n = int(input())
    num_list = list(map(int, input().split()))

    answer = []

    for i in range(len(num_list)) :
        if i == 0 :
            answer.append(num_list[i])
        else :
            if num_list[i] > answer[-1] :
                answer.append(num_list[i])
            else :
                idx = bisect_left(answer, num_list[i])
                answer[idx] = num_list[i]

    print(len(answer))


solution()
