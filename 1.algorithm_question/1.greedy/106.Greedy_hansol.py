# Greedy Algorithm
# 병든 나이트
# https://www.acmicpc.net/problem/1783

N, M = map(int, input().split())
# 이동할 수 없는 경우
if N == 1: ans = 1
# 위로 두 칸 이동이 불가하므로 오른쪽으로 두 칸씩 이동, 모든 이동을 사용할 수 없으므로 최댓값은 4
elif N == 2: ans = min(4, (M + 1)//2)
# 모든 이동을 사용한 경우 7이고 그렇지 않은 경우 M이 답이지만 최댓값은 4로 제한
elif M < 7: ans = min(4, M)
# 7까지 5개 칸을 방문하고 이후로는 1칸 씩 방문이 가능
else: ans = M - 2
print(ans)