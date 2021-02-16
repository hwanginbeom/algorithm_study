# 예산
def binary_search(_list, target) :
    answer = 0

    start = 1
    end = _list[-1]

    # 이분탐색
    while start <= end :
        _sum = 0
        mid = (start + end) // 2

        for i in _list :
            if i <= mid :
                _sum += i
            else :
                _sum += mid

        if _sum == target :
            return mid
        elif _sum > target :
            end = mid - 1
        else :
            answer = mid
            start = mid + 1

    return answer


def solution() :
    n = int(input())
    deposit_list = list(map(int, input().split()))
    upper_limit = int(input())

    deposit_list.sort()

    print(binary_search(deposit_list, upper_limit))


solution()

# 처음에 틀렸던 이유
# 이분탐색 시작범위 start 변수를 1로 주지않고 배열의 최솟값으로 넣었다.
# 배열의 값들이 다 비슷비슷한 경우 start 값이 빠르게 end 값을 넘어가기 때문에
# 정답을 찾지 못하고 이분탐색을 종료
