from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# relation_T = [list(x) for x in zip(*relation)]

col = len(relation[0]) #4
row = len(relation) #6


result = []
for i in range(1, col+1): #combinations 하려는 순열 수
    comb_list = list(combinations(range(col), i))

    for comb in comb_list: #순열 한 케이스
        a = [''.join([item[j] for j in comb]) for item in relation]
        if len(set(a)) == row:
            result.append(comb)


answer = set(result)
# 만족하는 전체 조합에서 이미 포함된 결과는 제거
# set 타입에서는 discard 가능, remove로 하면 꼬인당...
for i in range(len(result)):
    for j in range(i+1, len(result)):
        if len(set(result[i]) & set(result[j])) == len(result[i]):
            answer.discard(result[j])
print(len(answer))
