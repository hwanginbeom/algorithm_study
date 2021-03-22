stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

def check(stones, k, mid):
    count = 0
    for i in stones:
        if i < mid:
            count += 1
        else:
            count = 0
        if count == k:  # 뛰어 넘어야 하는 stone의 개수가 k개가 되면 건널 수 없다.
            return 0
    return 1

def solution(stones, k):
    answer = 0
    left = 1  # 가능한 최소 인원 1명
    right = max(stones) + 1  # 가능하지 않은 최소 인원 (= 가능한 최대 인원 +1)

    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2
        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    answer = left - 1  # 마지막에 가능했던 인원
    return answer


# 정확성은 완벽 하지만 효율성은 개똥
#
# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# k = 3
#
# result = []
# for i in range(0, len(stones)-k+1):
#     result.append(max(stones[i:i+k]))
# print(min(result))
