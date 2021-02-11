# 2021-02-11

# 출처 : https://www.acmicpc.net/problem/1697

# 숨바꼭질

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

from collections import deque

def bfs():
    queue=deque()
    queue.append(N)

    while queue:
        x=queue.popleft()
        if x==K:
            print(time[x])
            break
        for i in (x-1,x+1,2*x):
            if 0<=i<=value and not time[i]:
                time[i]=time[x]+1
                queue.append(i)

value=100000
time=[0]*(value+1)
N,K=map(int,input().split())

bfs()
