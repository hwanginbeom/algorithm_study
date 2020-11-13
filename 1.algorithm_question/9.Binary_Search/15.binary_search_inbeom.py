# 1654
n,m = list(map(int,input().split(' ')))
array = []
for i in range(n):
    array.append(int(input()))

start = 0
end = max(array)

restult = 0

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치
    lines = 0  # 랜선 수
    for i in array:
        lines += i // mid  # 분할 된 랜선 수

    if lines >= m:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)