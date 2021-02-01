# 2021-02-01

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17682

# 다트 게임

s=input()
def solution(s):
    score=[]
    number=''
    for i in s:
        if i.isdigit():
            number+=i
        elif i =='S':
            score.append(int(number))
            number=''
        elif i =='D':
            score.append(int(number)**2)
            number=''
        elif i =='T':
            score.append(int(number)**3)
            number=''
        elif i=='*':
            if len(score)>1:
                score[-2]*=2
            score[-1]*=2
            number=''
        elif i=='#':
            score[-1]*=(-1)

    return sum(score)

print(solution(s))


