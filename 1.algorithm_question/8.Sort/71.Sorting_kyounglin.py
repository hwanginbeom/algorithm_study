# 2021-02-14

# 출처 : https://www.acmicpc.net/problem/1764

# 정렬 - 듣보잡

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

n,m=map(int,input().split())
array1=[]
array2=[]
for _ in range(n):
    array1.append(input())
array1=set(array1)

for _ in range(m):
    array2.append(input())
array2=set(array2)


answer=[]

# 교집합 구하기
for i in array1:
    if i in array2:
        answer.append(i)

print(len(answer))
for i in sorted(answer):
    print(i,end='\n')


