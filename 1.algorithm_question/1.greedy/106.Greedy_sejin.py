import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n:세로, m:가로

# 2위 1오른 // 1위 2 오른 // 1아래 2오른 // 2아래 1오른

# 세로 1이면, 아무런 이동 없다
if n == 1:
    count = 1

# 세로 2이면, 가로 길이에 따라 달라진다
elif n == 2:
    count = min(4, (m+1) // 2)

# 세로 3 이상인데 가로 7보다 작으면 4가지 경로 모두는 이용 못한다
elif m < 7:
    count = min(4, m)

else:
    count = (m-2)

print(count)
