# 2021-01-26

# 출처 : https://www.acmicpc.net/problem/1747

# 소수&팰린드룸

# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다.
# 예를 들어 79,197과 324,423 등이 팰린드롬 수이다
# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

# 소수의 판별 (2이상의 자연수)
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True # 소수 판별

n=int(input())
for i in range(n,10000000):
    if str(i) == str(i)[::-1]:
        if is_prime_number(i):
            if i == 1:
                print(2)
                break
            print(i)
            break
