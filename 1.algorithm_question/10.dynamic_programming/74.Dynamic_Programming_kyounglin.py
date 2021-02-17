# 2021-02-27

# 출처 : https://www.acmicpc.net/problem/2579

# 다이나믹 프로그래밍 - 계단 오르기

# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
# 계단 오르는 데는 다음과 같은 규칙이 있다.
#
# 1) 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2) 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3) 마지막 도착 계단은 반드시 밟아야 한다.

# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다.
# 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n=int(input())

stairs=[0]*301 # 런타임 에러의 원인...ㅂㄷㅂㄷ 이유를 모르겠다....ㅠ
for i in range(n):
    stairs[i]=int(input())

# stairs=[0]*301없으면 런타임 에러....ㅠ
d=[0]*301

d[0]=stairs[0]
d[1]=max(stairs[0]+stairs[1],stairs[1])
d[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,n):
    d[i]=max(d[i-2]+stairs[i],d[i-3]+stairs[i]+stairs[i-1])

print(d[n-1])

# 런타임 에러....
d=[]

d.append(stairs[0]) # 첫 계단
d.append(max(stairs[0]+stairs[1],stairs[1])) # 두번째 합은 -> 두번 째 계단 or 첫계단 밟고 두번째 계단 이동
d.append(max(stairs[0]+stairs[2],stairs[1]+stairs[2])) # 3번째 합은 -> 첫번째에서 3번째로 2 step or 두번째에서 3번째로 1 step

for i in range(3,n):
    d.append(max(d[i-2]+stairs[i],d[i-3]+stairs[i]+stairs[i-1]))
# dp[i] = dp[i-1] + arr[i]이면 i칸 전에 i-1계단을 밟았기 때문에 3step 가능성 존재
# 그러므로 d[i-3]+stairs[i]+stairs[i-1] # 3칸 연속 방지 i-3 - i-1 - i

print(d.pop())
