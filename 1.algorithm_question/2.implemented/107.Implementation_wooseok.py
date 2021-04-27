# 파일 정리
# https://www.acmicpc.net/problem/20291


def solution() :
    n = int(input())
    FNE_dict = {}

    for _ in range(n) :
        string = input()
        split_list = string.split('.')

        if split_list[1] in FNE_dict.keys() :
            FNE_dict[split_list[1]] += 1
        else :
            FNE_dict[split_list[1]] = 1

    FNE_dict = sorted(FNE_dict.items(), key = lambda x : x[0])

    for i in FNE_dict :
        print(i[0], i[1])


solution()
