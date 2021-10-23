# 2021-10-21

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

# 순위 검색

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250",
         "- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


import bisect

def solution(info,query):
    answer=[]

    language = ['cpp', 'java', 'python', '-']
    position = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    soul_food = ['chicken', 'pizza', '-']

    table = {}
    for l in language:
        for p in position:
            for c in career:
                for s in soul_food:
                    string=l+p+c+s
                    table[string]=[]

    for candidate in info:
        string = candidate.split(' ')
        language = [string[0], '-']
        position = [string[1], '-']
        career = [string[2], '-']
        soul_food = [string[3], '-']

        for l in language:
            for p in position:
                for c in career:
                    for s in soul_food:
                        key=l+p+c+s
                        table[key].append(int(string[4]))

    for key, value in table.items():
        table[key]=sorted(value)

    for candidate in query:
        person,score=candidate.replace(' and ','').split(' ')
        score=int(score)
        size=len(table[person])
        num = size - bisect.bisect_left(table[person], score, lo=0, hi=size)
        answer.append(num)

    return answer

print(solution(info,query))
