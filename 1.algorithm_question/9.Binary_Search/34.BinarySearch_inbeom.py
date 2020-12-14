# 2110(이진탐색) - 공유기 설치

n, c = map(int,input().split())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()
st = 1
en = s[-1] - s[0]
res = 0
while st <= en:
    mid = (st + en) // 2
    cnt = 1
    ih = s[0]
    for i in range(1,n):
        if mid <= s[i] - ih:
            cnt += 1
            ih = s[i]
    if cnt >= c:
        res = mid
        st = mid + 1
    else:
        en = mid-1
print(res)