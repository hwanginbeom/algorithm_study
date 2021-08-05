# 단어 정렬
# https://www.acmicpc.net/problem/1181


def solution() :
    n = int(input())
    word_list = []

    for _ in range(n) :
        word_list.append(input())

    # 중복 제거
    word_list = list(set(word_list))

    # 정렬
    sorted_list = sorted(word_list, key = lambda x : (len(x), x))

    for i in sorted_list :
        print(i)


solution()
