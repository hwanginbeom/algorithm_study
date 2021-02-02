# 2021-02-02

# 출처 : https://www.acmicpc.net/problem/1744

# 수 묶기

# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다.
# 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
# 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다.
# 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.
# 리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
# 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.


import sys
input=sys.stdin.readline
n=int(input())
plus=[]
zero_minus=[]
answer=0
for _ in range(n):
    x=int(input())
    if x<=0:
        zero_minus.append(x)
    elif x==1: # 1은 곱해도 의미가 없음 그냥 더해버리기~~!
        answer+=1
    else:
        plus.append(x)


# 정렬
zero_minus.sort()
plus.sort(reverse=True)


# 양수

if len(plus)==1:
    answer+=plus[0]
elif len(plus)>1:
    for i in range(0,len(plus)-1,2):
        answer+=plus[i]*plus[i+1]

    if len(plus)%2!=0:
        answer+=plus[-1]

# 음수
# 0은 가장 마지막에 곱해야함

if len(zero_minus)==1:
    answer+=zero_minus[0]
elif len(zero_minus)>1:
    for i in range(0,len(zero_minus)-1,2):
        answer += zero_minus[i] * zero_minus[i + 1]

    if len(zero_minus)%2!=0:
        answer+=zero_minus[-1]


print(answer)



