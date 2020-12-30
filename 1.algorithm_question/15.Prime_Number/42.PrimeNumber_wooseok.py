# 직각삼각형
import math


def solution() :
    while True :
        side = list(map(int, input().split()))
        side.sort()

        if 0 in side :
            break

        if side[2] == math.sqrt(side[0] ** 2 + side[1] ** 2) :
            print('right')
        else :
            print('wrong')


solution()
