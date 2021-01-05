n = int(input())
for _ in range(n):
    H, W, N = map(int, input().split())
    print([ str(i2+1)+str(i+1).zfill(2) for i in range(W) for i2 in range(H)][N-1])
