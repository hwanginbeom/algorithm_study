# 2021-05-27

# 출처 : https://www.acmicpc.net/problem/9465

# 스티커

T=int(input())
for _ in range(T):
    n=int(input())

    array = [list(map(int, input().split())) for _ in range(2)]
    # 시작
    array[0][1]+=array[1][0]
    array[1][1]+=array[0][0]

    for i in range(2,n):
        array[0][i]+=max(array[1][i-1],array[1][i-2])
        array[1][i] += max(array[0][i - 1], array[0][i - 2])
    # 위 or 아래시작 중 큰값을 출력
    print(max(array[0][i],array[1][i]))