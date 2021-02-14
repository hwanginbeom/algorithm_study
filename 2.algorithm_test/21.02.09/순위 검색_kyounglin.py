# 2021-02-09

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/72412

# 순위 검색 - 모르겠어서 https://pacientes.github.io/posts/2021/02/algorithm_programmers_72412/ 사이트 참고

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

import bisect


def solution(info,query):
    answer=[]

    language=['cpp', 'java', 'python', '-']
    position=['backend', 'frontend', '-']
    career=['junior', 'senior', '-']
    soul_food=['chicken', 'pizza', '-']

    table={} # 모든 경우의 수에 대한 딕셔너리 생성
    for l in language:
        for p in position:
            for c in career:
                for s in soul_food:
                    string=l+p+c+s
                    table[string]=[]

    for candidate in info:
        string=candidate.split(' ')
        language=[string[0],'-']
        position=[string[1],'-']
        career=[string[2],'-']
        soul_food=[string[3],'-']

        for l in language: # 모든 조합을 비교해 본 뒤 table에서 key에 해당 되는 조합이 나오면 해당 점수 넣기
            for p in position:
                for c in career:
                    for s in soul_food:
                        key=l+p+c+s
                        table[key].append(int(string[4]))

    for key, value in table.items(): # score를 기준으로 오름차순
        table[key]=sorted(value)

    for candidate in query:
        person,score=candidate.replace(' and ','').split(' ')
        score=int(score)
        size=len(table[person])
        num=size-bisect.bisect_left(table[person],score,lo=0,hi=size) #배열 이진 분할 알고리즘
        # 리스트 길이에서 특정 점수가 처음 나타나는 위치를 빼줌
        # 숫자가 오름차순으로 정렬된 배열에서 X라는 숫자를 찾는 효율적인 방법으로 binary search를 사용할 수 있습니다. 이때, 배열에 X가 없을 수도 있으므로, 배열에서 X보다 크거나 같은 숫자가 처음 나타나는 위치를 찾아야 하며, 이는 lower bound를 이용
        answer.append(num)


    return answer

print(solution(info,query))

# bisect_left(a, x, lo=0, hi=len(a))¶
# 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다.
# 매개 변수 lo 와 hi는 고려해야 할 리스트의 부분집합을 지정하는 데 사용될 수 있습니다;
# 기본적으로 전체 리스트가 사용됩니다.
# x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다.
# 반환 값은 a가 이미 정렬되었다고 가정할 때 list.insert()의 첫 번째 매개 변수로 사용하기에 적합합니다.
# hi -> 영역 제한
# 반환된 삽입 위치 i는 배열 a를 이분하여, 왼쪽은 all(val < x for val in a[lo:i]), 오른쪽은 all(val >= x for val in a[i:hi])이 되도록 만듭니다.