# 배열 합치기
# https://www.acmicpc.net/problem/11728


def solution() :
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    index_a = 0
    index_b = 0
    answer = []

    while index_a < n and index_b < m :
        if a[index_a] <= b[index_b] :
            answer.append(a[index_a])
            index_a += 1
        else :
            answer.append(b[index_b])
            index_b += 1

    if index_a == n :
        answer.extend(b[index_b:])
    else :
        answer.extend(a[index_a:])

    for i in answer :
        print(i, end = ' ')


solution()
