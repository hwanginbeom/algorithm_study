# 9. 기타 알고리즘
# 소수 부분 문자열
# https://www.acmicpc.net/problem/5636

import math

# 소수 판별 함수 정의
def is_prime_number(x):
    # 100000보다 작아야하는 조건 추가
    if x < 100000:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    return False

# 입력값 받기
lst = []
while True:
    data = input()
    # 0이 입력되면 멈추기
    if data == '0':
        break
    lst.append(data)

for data in lst:
    # 최댓값을 찾기 위한 타겟 설정
    target = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            # [i:j] = [0:1], [0:2], ... , [0:끝값], [1:2], [1:3], ...
            if is_prime_number(int(data[i:j])):
                # 최댓값으로 초기화
                target = max(target, int(data[i:j]))
    print(target)
