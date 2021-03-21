# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062


def solution(stones, k):
    answer = 0
    _max = '0' * k

    while True:
        str_stones = ''.join(list(map(str, stones)))
        # print(str_stones)

        if _max in str_stones:
            break

        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1
        answer += 1

    return answer


# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones = [200000000, 0, 200000000, 1, 0, 200000000]
k = 3
print(solution(stones, k))

# 효율성 제로, 정확성 에러
