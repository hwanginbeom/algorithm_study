# 9. 기타 알고리즘
# Prime Number & Palindrome
# https://www.acmicpc.net/problem/1747

import math

# 소수 판별 함수를 정의 (강의 참고)
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 입력한 수보다 크고 입력값보다 충분히 큰 수를 끝 값으로 설정
for _ in range(int(input()), 10000000):
    # Palindrome 수인지 확인
    if str(_) == str(_)[::-1]:
        # 소수인지 확인
        if is_prime_number(_):
            # 1을 입력하면 2가 나오는 예외값을 설정
            if _ == 1:
                print(2)
                break
            # Palindrome, 소수를 만족하면 해당 수를 출력
            print(_)
            break
