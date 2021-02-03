# 구현
# 방 번호
# https://www.acmicpc.net/problem/1475

# 소수점 올림을 위한 라이브러리
import math

N = input()
check = []
# 6, 9를 제외한 숫자들의 개수를 리스트에 입력
for i in [0,1,2,3,4,5,7,8,0]:
    check.append(N.count(str(i)))

# 6, 9를 뒤집을 수 있는 조건을 적용해 필요한 세트 수를 리스트에 입력
check.append(math.ceil((N.count('6') + N.count('9')) / 2))
# 가장 많이 필요한 수의 세트 수를 출력
print(max(check))