# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
import copy


def get_jaccard(string):
    alpha_list = []

    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha() :
            alpha_list.append(string[i:(i + 2)])

    return alpha_list


def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    alpha_list1 = get_jaccard(str1)
    alpha_list2 = get_jaccard(str2)

    # 리스트 복사하여 사용
    copy_list1 = copy.deepcopy(alpha_list1)
    copy_list2 = copy.deepcopy(alpha_list2)

    # 교집합 구하기
    A = 0
    intersection_list = []

    for alpha in alpha_list1 :
        if alpha in copy_list2 :
            A += 1
            intersection_list.append(alpha)
            copy_list2.remove(alpha)

    # 합집합 구하기
    for i in intersection_list :
        copy_list1.remove(i)

    alpha_list2.extend(copy_list1)
    B = len(alpha_list2)

    if B == 0:
        answer = 1
    else:
        answer = A / B

    return int(answer * 65536)


str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2))
