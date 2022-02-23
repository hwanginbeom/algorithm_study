#백준 11728번
#배열 합치기

import sys
N,M=map(int,sys.stdin.readline().split())

#2개리스트 입력받기
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

#오름차순으로 정렬
list= sorted(a+b)

#리스트 형식을  str로 바꾸고 띄어쓰기를 포함해 출력
print(" ".join(map(str.list)))

