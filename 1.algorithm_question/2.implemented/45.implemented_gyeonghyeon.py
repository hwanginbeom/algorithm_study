n = int(input())
for _ in range(n):
    H, W, N = map(int, input().split())
    list_1 = [ str(i2+1)+str(i+1).zfill(2) for i in range(W) for i2 in range(H)]
    print(list_1[N-1])