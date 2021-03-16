# 선입후출 => 스택

n = int(input())
stack = []
answer = 0

for i in range(n):
    data = list(map(int, input().split()))

    # 과제 입력 받기
    if len(data) == 3:
        stack.append([data[1], data[2]]) # 만점 점수, 해결 시간

    # 돌 때마다 시간 줄여주기
    if stack:
        stack[-1][1] -= 1

        # 과제 해결 시간이 채워졌다면
        if stack[-1][1] == 0:
            answer += stack.pop()[0]

print(answer)
