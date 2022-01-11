# 나이순 정렬
# https://www.acmicpc.net/problem/10814


def solution() :
    n = int(input())
    member_list = []

    for i in range(n) :
        age, name = input().split()
        age = int(age)

        member_list.append([i, age, name])

    sorted_list = sorted(member_list, key = lambda x : (x[1], x[0]))

    for i in sorted_list :
        print(i[1], i[2])


solution()
