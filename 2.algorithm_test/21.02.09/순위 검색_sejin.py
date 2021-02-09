# 재귀함수

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

info_table = []
for i in range(len(info)) :
    info_table.append(info[i].split(' '))
# print(info_table)


query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

query_table = []
for i in range(len(query)) :
    sentence = query[i].replace('and ','') #마지막 숫자앞엔 and가 없어서
    query_table.append(sentence.split(' '))
# print(query_table)

answer = []
for i in range(len(query_table)) : #기준 찾으려는거
    count = 0
    for info in info_table : #범위
        if (query_table[i][0] in info[0]) or (query_table[i][0]=='-') :
            if (query_table[i][1] in info[1]) or (query_table[i][1]=='-') :
                if (query_table[i][2] in info[2]) or (query_table[i][2]=='-') :
                    if (query_table[i][3] in info[3]) or (query_table[i][3]=='-') :
                        if (int(query_table[i][4]) <= int(info[4])) or (query_table[i][4]=='-') :
                            count += 1
    answer.append(count)
print(answer)

