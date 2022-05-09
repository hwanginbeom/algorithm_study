# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
import re


def solution(s):
    answer = []

    split_list = s.split('},{')
    num_list = []

    for l in split_list:
        temp = re.sub('[^0-9]', ' ', l)
        num_list.append(temp.split())

    num_list = sorted(num_list, key=lambda x: len(x))

    for i in range(len(num_list)):
        if i == 0:
            answer.append(int(num_list[i][0]))
        else:
            answer.append(int(list(set(num_list[i]) - set(num_list[i - 1]))[0]))

    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
