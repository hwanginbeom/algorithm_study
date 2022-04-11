# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
import re, copy, math


# 다중집합 만들기
def make_multiple_list(string):
    multiple_list = []
    for i in range(len(string) - 1):
        multiple_list.append(string[i:i + 2])

    new_multiple_list = []
    for i in multiple_list:
        if not re.search('[^a-zA-Z]', i):
            new_multiple_list.append(i)

    return new_multiple_list


# 중복을 허용한 리스트 교집합
def list_intersection(li1, li2):
    intersection_list = []

    for i in li1:
        if i in li2:
            intersection_list.append(i)
            del li2[li2.index(i)]

    return intersection_list


# 중복을 허용한 리스트 합집합
def list_union(li1, li2):
    union_list = []

    for i in li1:
        if i in li2:
            union_list.append(i)
            del li2[li2.index(i)]
        else:
            union_list.append(i)

    for i in li2:
        if i in li1:
            union_list.append(i)
            del li1[li1.index(i)]
        else:
            union_list.append(i)

    return union_list


def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    multiple_list1 = make_multiple_list(str1)
    multiple_list2 = make_multiple_list(str2)

    intersection_list = list_intersection(copy.deepcopy(multiple_list1), copy.deepcopy(multiple_list2))
    union_list = list_union(multiple_list1, multiple_list2)

    if len(union_list) == 0:
        jaccard_similarity = 1 * 65536
    else:
        jaccard_similarity = math.floor((len(intersection_list) / len(union_list)) * 65536)

    answer = jaccard_similarity
    return answer


str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2))
