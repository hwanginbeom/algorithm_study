# 2021-02-05

# 출처 : https://www.acmicpc.net/problem/1914

# 하노이 탑

# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.
#
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.
#
# 아래 그림은 원판이 5개인 경우의 예시이다.




# start -> 출발지 end -> 목적지 other -> 2번째 기둥

def hanoi_top(n,start,end,other):
    if n==1:
        print(start, end)
    else:
        hanoi_top(n-1, start, other, end) # 맨 아래 원반 빼고 나머지 보조 기둥으로
        print(start, end) # 하나 남은거 목표로 이둥
        hanoi_top(n-1, other, end, start) # 보조기둥에 있는 원반들이 이제 시작지점이됨


n = int(input())
print(2**n-1)
if n<=20:
    hanoi_top(n,1,3,2)