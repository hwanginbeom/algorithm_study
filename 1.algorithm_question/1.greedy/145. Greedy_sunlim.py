# 백준 11047번
# 동전 종류 N, 동전 가치의 합을 K로 만들어야함 > 필요한 개수 최솟값 구해라


n,k =map(int,input().split())
m=[]
num=0
for i in range(n):
    m.append(int(input()))
for i in range(n-1,-1,-1):
    if k == 0:
        break
    if m[i]>k:
        continue
    num +=k //m[i]
    k%= m[i]
print(num)