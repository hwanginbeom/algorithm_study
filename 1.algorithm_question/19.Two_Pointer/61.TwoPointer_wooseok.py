# 소수의 연속합
import math


def solution() :
    n = int(input())

    # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    array = [True for i in range(n + 1)]

    # 에라토스테네스의 체 알고리즘 수행
    # 2부터 n의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        # i가 소수인 경우(남는 수인 경우)
        if array[i] is True:
            # i를 제외한 모든 배수를 지우기
            j = 2

            while i * j <= n:
                array[i * j] = False
                j += 1

    # 소수 리스트 만들기
    prime_list = []
    for i in range(2, len(array)) :
        if array[i] :
            prime_list.append(i)

    count = 0
    interval_sum = 0
    end = 0

    # 투 포인터를 이용한 연속된 수의 합 구하기
    # start를 차례대로 증가시키며 반복
    for start in range(len(prime_list)):
        # end를 가능한 만큼 이동시키기
        while interval_sum < n and end < len(prime_list):
            interval_sum += prime_list[end]
            end += 1

        # 부분합이 m일 때 카운트 증가
        if interval_sum == n:
            count += 1

        interval_sum -= prime_list[start]

    print(count)


solution()
