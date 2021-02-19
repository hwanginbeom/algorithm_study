T = int(input())

for test_case in range(T):
    N = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    possible = [[int(1e9)] * (N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            if i != j:
                diff = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])
                if diff <= 1000:
                    possible[i][j] = 1

    for k in range(N+2):
        for a in range(N+2):
            for b in range(N+2):
                possible[a][b] = min(possible[a][b], possible[a][k] + possible[k][b])

    if possible[0][N+1] == int(1e9):
        print("sad")
    else:
        print("happy")
