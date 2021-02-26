import math

t = int(input()) # t:테스트케이스

for _ in range(t) :
    n = int(input())
    array = [True for i in range(n + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True:  # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(n//2, 1, -1):
        if array[i]:
            if array[n-i]:
                print(i, n-i)
                break


# 왜 얘는 9%에서 틀리는지 이유를 모르겠네..;
# import math
#
# def is_prime_number(x) :
#     if x == 1 :
#         return False
#     else :
#         for i in range(2, int(math.sqrt(x)) + 1) :
#             if x % i == 0 :
#                 return False
#         return True
#
# t = int(input()) # t:테스트케이스
# for _ in range(t) :
#     n = int(input())
#
#     for i in range(n//2, 1, -1):
#         if is_prime_number(i):
#             if is_prime_number(n-i):
#                 print(i, n-i)
#                 break