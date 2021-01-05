N = int(input())

for _ in range(N) :
    h, w, n = map(int, input().split())
    print([ str(i2+1)+str(i+1).zfill(2) for i in range(w) for i2 in range(h)][n-1])
