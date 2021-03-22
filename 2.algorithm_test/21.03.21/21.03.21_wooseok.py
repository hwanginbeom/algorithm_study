# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062


def check(mid, stones, k) :
    cnt = 0

    # mid 값이 니니즈 친구들의 수
    # 연속된 디딤돌의 개수가 k개 이상이고 횟수가 0 이하인 구간 찾기
    for stone in stones :
        if stone - mid <= 0 :
            cnt += 1
        else :
            cnt = 0

        if cnt >= k :
            return True

    return False


def solution(stones, k) :
    # 디딤돌의 횟수를 이용하여
    # 니니즈 친구들의 수의 범위 선정
    start, end = 1, 200000000

    while start <= end :
        mid = (start + end) // 2

        if check(mid, stones, k) :
            end = mid - 1
        else :
            start = mid + 1

    return end + 1


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))

# 탐색시간이 매우 길어질 것이라고 예상되면 이분탐색을 떠올려보기
# 이분탐색으로 찾는 것이 니니즈 친구들의 수라니...

# 니니즈 친구들의 수를 탐색하여
# 연속된 디딤돌의 횟수가 0 이하가 되는 구간을 찾는다.
# 최대로 뛰어넘을 수 있는 디딤돌 개수인 k와 구간의 디딤돌 개수를 비교하여
# k 보다 크면 니니즈 친구들의 수를 줄이고, k 보다 작으면 니니즈 친구들의 수를 늘여서 탐색한다.
