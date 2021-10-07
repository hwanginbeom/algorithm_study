# 모음사전
# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    answer = 0

    vowel_list = ['A', 'E', 'I', 'O', 'U']
    dict_list = []

    # 전체 단어 조합하기
    for i in range(1, 6):
        for j in product(vowel_list, repeat=i):
            dict_list.append(''.join(list(j)))

    dict_list.sort()
    answer = dict_list.index(word) + 1

    return answer


word = "EIO"
print(solution(word))
