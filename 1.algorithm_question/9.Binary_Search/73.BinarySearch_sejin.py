n = int(input())
array = list(map(int, input().split()))
m = int(input())

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x >= mid:
            total += mid
        else:
            total += x

    # 오른쪽 부분 탐색
    if total <= m:
        start = mid + 1
        result = mid
    # 왼쪽 부분 탐색
    else:
        end = mid - 1

print(result)
