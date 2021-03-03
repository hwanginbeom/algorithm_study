# 2021-03-03

# 출처 : https://www.acmicpc.net/problem/11286

# 절대값 힙

# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
# 1.배열에 정수 x (x ≠ 0)를 넣는다.
# 2.배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import heapq,sys
input=sys.stdin.readline #시간초과 나서 적용

n=int(input())
array=[]

for _ in range(n):
    value=int(input())
    if value==0: # 값이 0일 경우
        if array:
            print(heapq.heappop(array)[1])
        else: # 리스트가 비었을 때 0출력
            print(0)
    else:
        heapq.heappush(array,(abs(value),value))
