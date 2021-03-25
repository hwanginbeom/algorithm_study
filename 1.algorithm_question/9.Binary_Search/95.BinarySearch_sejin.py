import sys
input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))

start = 0
end = len(data)-1
sum1 = abs(data[start] + data[end])
s = start
e = end

while start < end:
    sum2 = data[start] + data[end]

    if abs(sum2) < sum1:
        cs = start
        ce = end
        sum1 = abs(sum2)

        if sum1 == 0:
            break

    # 합이 0보다 큰 경우, 왼쪽 부분 탐색
    if sum2 > 0:
        end -= 1

    # 합이 0보다 작은 경우, 오른쪽 부분 탐색
    else:
        start += 1

print(data[cs], data[ce])