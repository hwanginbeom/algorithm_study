import sys

input = sys.stdin.readline
n, h = map(int, input().split())
huddle = [0] * h

for i in range(n // 2):
    huddle[int(input())] -= 1
    print(huddle)
    huddle[h - int(input())] += 1
    print(huddle)

minn, numm = n // 2, 0
hud = n // 2

for i in huddle:
    hud += i
    if hud < minn:
        minn = hud
        numm = 1
    elif hud == minn:
        numm += 1

print(minn, numm)
