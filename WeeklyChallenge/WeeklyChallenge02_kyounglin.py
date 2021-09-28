# 2021-09-28

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/83201

# 위클리 챌린지 - 2주차_상호평가

scores=[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

def solution(scores):

    t=[[] for _ in range(len(scores))]

    # 각 학생들의 번호를 모아둠 ex) 0번학생의 점수들은 t의 0번 리스트에 있음
    for i in range(len(scores)):
        for j in range(len(scores[i])):
            t[i].append(scores[j][i])

    avg=[] # 각 학생들의 점수 평균을 담을 리스트

    for st in range(len(t)):
        check=[]
        for sc in range(len(t)):
            if st==sc:
                if (max(t[st])==t[st][sc] and t[st].count(max(t[st]))==1) or (min(t[st])==t[st][sc] and t[st].count(min(t[st]))==1):
                    pass
                else:
                    check.append(t[st][sc])
            else:
                check.append(t[st][sc])
        avg.append(sum(check)/len(check))

    answer=''
    # 점수 부여
    for k in avg:
        if k>=90:
            answer+='A'
        elif k>=80:
            answer+='B'
        elif k>=70:
            answer+='C'
        elif k>=50 :
            answer+='D'
        else:
            answer+='F'

    return answer

print(solution(scores))