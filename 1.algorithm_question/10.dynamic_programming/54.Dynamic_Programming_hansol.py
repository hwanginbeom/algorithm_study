# Dynamic Programming
# https://www.acmicpc.net/problem/9095
# 정수 n이 주어졌을 때,
# n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# Sol 1
# using top down dynamic programming

# 0으로 이루어진 리스트를 생성
d = [0] * 11


def n123(x):
    # x = 1, 2, 3 일 때의 값을 지정
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    # 원소가 0이 아닌 경우에는 다시 함수를 돌리는 것이 아니라 그 값 자체를 return
    if d[x] != 0:
        return d[x]
    # 점화식을 만들어 적용
    d[x] = n123(x - 1) + n123(x - 2) + n123(x - 3)
    return d[x]


# input 값을 받아 출력
T = int(input())

for i in range(T):
    print(n123(int(input())))



# Sol2
# using bottom up dynamic programming

# 0으로 이루어진 리스트를 생성
n = 10
d = [0] * (n+1)

# 1, 2, 3 일 때의 초기값 설정
d[1] = 1
d[2] = 2
d[3] = 4

# 모든 경우에 대해 점화식을 적용해 리스트를 완성
for i in range(4, n+1):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

# input 값에 맞는 해당 원소를 출력
for i in range(int(input())):
    print(d[int(input())])
