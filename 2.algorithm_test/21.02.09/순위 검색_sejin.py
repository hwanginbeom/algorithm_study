info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

import re, collections, itertools, bisect

def solution(info, query):
    answer = []
    info_hash = collections.defaultdict(list)

    for v in info:
        arr = v.split()
        condition, score = tuple(sorted(arr[:-1])), int(arr[-1])
        info_hash[()].append(score)
        info_hash[condition].append(score)
        for n in range(1,4):
            for com in itertools.combinations(condition, n):
                info_hash[com].append(score)

    for key in info_hash.keys():
        info_hash[key].sort()

    for i, v in enumerate(query):
        arr = v.replace('and','').replace('-', '').split()
        condition, score = tuple(sorted(arr[:len(arr)-1])), int(arr[-1])
        scores = info_hash[condition]

        if len(scores) == 0:
            answer.append(0)
        else:
            i = bisect.bisect_left(scores, score)
            answer.append(len(scores) - i)
    return answer
print(solution(info,query))




# 정확도만 맞은 코드
#
# def solution(info, query):
#     info_table = []
#     for i in range(len(info)):
#         info_table.append(info[i].split(' '))
#
#     query_table = []
#     for i in range(len(query)):
#         sentence = query[i].replace('and ', '')
#         query_table.append(sentence.split(' '))
#
#     answer = []
#     for i in range(len(query_table)):
#         count = 0
#         for info in info_table:
#             if (query_table[i][0] in info[0]) or (query_table[i][0] == '-'):
#                 if (query_table[i][1] in info[1]) or (query_table[i][1] == '-'):
#                     if (query_table[i][2] in info[2]) or (query_table[i][2] == '-'):
#                         if (query_table[i][3] in info[3]) or (query_table[i][3] == '-'):
#                             if (int(query_table[i][4]) <= int(info[4])) or (query_table[i][4] == '-'):
#                                 count += 1
#         answer.append(count)
#     return answer
#
# print(solution(info,query))