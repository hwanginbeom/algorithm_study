## 백준 10814번 나이순 정렬

#1. 리스트 형태로 나이와 이름을 입력받고
#2. 리스트에서 나이를 기준으로 오름차순으로 정렬 한다.

import sys
input=sys.stdin.readline()

N=int(input()) #온라인 저지 회원수, 정수형으로 받는거 잊지말고!

user=[]

#리스트형태로 입력받기!
for _ in range (N):
    user.append(list(input().split())) #나이와 이름 공백으로 구분

#나이를 기준으로 정렬
user.sort(key=lambda a:int(a[0])) #각 행의 첫번째 인덱스를 기준으로, 즉 나이를 기준으로 정렬!

#출력
for i in range(N):
    print(user[i][0],user[i][1]) #순서대로 출력력