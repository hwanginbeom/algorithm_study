# 등수 매기기
import sys


def solution() :
    n = int(sys.stdin.readline())
    rank_list = []

    for _ in range(n) :
        rank = int(sys.stdin.readline())
        rank_list.append(rank)

    rank_list.sort()
    answer = 0

    for i in range(len(rank_list)) :
        answer += abs(rank_list[i] - (i + 1))

    print(answer)


solution()
