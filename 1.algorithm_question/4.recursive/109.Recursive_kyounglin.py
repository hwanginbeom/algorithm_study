# 2021-05-06

# 출처 : https://www.acmicpc.net/problem/1780

# 종이의 개수

import sys
input=sys.stdin.readline


from itertools import chain # 이차원 리스트 -> 일차원 리스트로

# n=len(paper)
def solution(paper):
    global minus_one,zero,plus_one
    n=len(paper)

    if len(set(chain.from_iterable(paper)))==1: # -1,0,1 셋중 하나로 통일 되어 있는 경우 - 무조건 종이는 +1
        if paper[0][0]==-1:
            minus_one+=1
        elif paper[0][0]==0:
            zero+=1
        else:
            plus_one+=1
    else:
        if n!=3: # 종이의 한 변이 3^n 인 경우 재귀를 통해 반복
            for i in range(0,n,n//3):
                for j in range(0,n,n//3): #+n//3을 통해 3의 배수씩 나누기
                    divide_paper=[k[j:j+n//3] for k in paper[i:i+n//3]] # 9개씩 종이를 나누기 - 종이가 같은 수가 아닐경우
                    solution(divide_paper)
        else: # 숫자가 9개로 되어있는경우
            for i in range(n):
                for j in range(n):
                    if paper[i][j]==-1:
                        minus_one+=1
                    elif paper[i][j]==0:
                        zero+=1
                    else:
                        plus_one+=1

N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]
minus_one,zero,plus_one=0,0,0
solution(array)
print(f'{minus_one}\n{zero}\n{plus_one}')



