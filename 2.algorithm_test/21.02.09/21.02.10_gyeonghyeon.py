def solution(numbers, hand):
    right_dict = {2:{2:0,3:1,5:1,6:2,8:2,9:3,'#':4,0:3},5:{2:1,3:2,5:0,6:1,8:1,9:2,'#':3,0:2},8:{2:2,3:3,5:1,6:2,8:0,9:1,'#':2,0:1},0:{2:3,3:4,5:2,6:3,8:1,9:2,'#':1,0:0}}
    left_dict =  {2:{1:1,2:0,4:2,5:1,7:3,8:2,'*':4,0:3},5:{1:2,2:1,4:1,5:0,7:2,8:1,'*':3,0:2},8:{1:3,2:2,4:2,5:1,7:1,8:0,'*':2,0:1},0:{1:4,2:3,4:3,5:2,7:2,8:1,'*':1,0:0}}
    answer = ''
    left = '*'
    right = '#'
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = num
        elif num in [3,6,9]:
            answer += 'R'
            right = num
        elif num in [2,5,8,0]:
            rightnum, leftnum = right_dict[num][right], left_dict[num][left]
            if rightnum < leftnum:
                answer += 'R'
                right = num
            elif leftnum < rightnum:
                answer +='L'
                left = num
            elif rightnum == leftnum:
                answer += hand[0].upper()
                if hand[0].upper() == 'R':
                    right = num
                else:
                    left = num
    print(answer)
    return answer
a = [2,0]
solution(a, 'right')

#--------------------------------------------#
# 순위검색#
# 효율성 실패 ㅠㅠ

import re
import copy
def solution(info, query):
    people = {idx:value.split(' ') for idx, value in enumerate(info)}
    check =  {idx:list(filter(lambda x: x != '', re.split('\s|and',value))) for idx, value in enumerate(query)}
    people2 = copy.deepcopy(people)
    answer = []
    for key, item in check.items():
        for idx,data in enumerate(item):
            if data == '-':
                continue
            else:
                if idx != (len(item)-1):
                    people = dict(filter(lambda x: x[1][idx] == data, people.items()))
                elif idx == (len(item)-1):
                    people = dict(filter(lambda x: int(x[1][idx]) >= int(data), people.items()))
        answer.append(len(people))
        people = people2
    print(answer)
    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
solution(info, query)