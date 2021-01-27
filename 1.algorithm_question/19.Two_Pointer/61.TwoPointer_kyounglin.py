# 2021-01-27

# 출처 : https://www.acmicpc.net/problem/1644

# 소수의 연속합

# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)

# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
# 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.


# 소수 가져오기

# 소수의 판별 (2이상의 자연수)

n=int(input())

# 소수의 판별 (2이상의 자연수)
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True # 소수 판별

data=[]
for i in range(2,n+1):
    if is_prime_number(i):
        data.append(i)

# 투 포인터 적용

count=0
interval_sum=0
end=0

# start를 차례대로 증가시키며 반복
for start in range(len(data)):
    # end를 가능한 만큼 이동시키기
    while interval_sum<n and end < len(data):
        interval_sum += data[end]
        end +=1
    # 부분합이 n일때 카운트 증가
    if interval_sum==n:
        count+=1
    interval_sum -=data[start]

print(count)