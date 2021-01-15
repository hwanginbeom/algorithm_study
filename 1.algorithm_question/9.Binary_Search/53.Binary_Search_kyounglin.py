# 2021-01-15

# 출처 : https://www.acmicpc.net/problem/10815

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n=int(input())
original=list(map(int,input().split()))
original.sort()
m=int(input())
card=list(map(int,input().split()))

for i in range(m):
    left,right,answer = 0,n-1,0
    while left<=right:
        mid=(left+right)//2
        if original[mid]==card[i]:
            answer=1
            break
        elif original[mid]<card[i]:
            left=mid+1
        else:
            right=mid-1


    print(answer,end=' ')


#----------------------------------------------------------------------

# 방법 2 : 이진탐색을 이용하지 않은 코드 for 문으로 구하기 --> 시간초과

answer=[]

for i in card:
    if i in original:
        answer.append(1)
    else:
        answer.append(0)

for j in answer:
    print(j,end=' ')


