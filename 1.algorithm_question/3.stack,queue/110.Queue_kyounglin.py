# 2021-05-08

# 출처 : https://www.acmicpc.net/problem/2346

# 풍선 터뜨리기

N=int(input())

idx=0 # 실제 인덱스 위치
result=[]
stack=list(map(int,input().split()))
index=[i for i in range(1,N+1)] # 풍선의 번호

# 처음 1번 풍선 터뜨리기
check=stack.pop(idx) # 풍선안에 적힌 종이
result.append(index.pop(idx)) # 정답에는 풍선의 번호가 들어가야함

while stack:
    if check<0: # 풍선 번호가 음수
        idx=(idx+check)%len(stack)
    else: # 풍선 번호가 양수
        idx=(idx+(check-1))%len(stack)

    check=stack.pop(idx)
    result.append(index.pop(idx))

for i in result:
    print(i,end=' ')