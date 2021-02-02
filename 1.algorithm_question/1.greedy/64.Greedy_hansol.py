# 그리디 알고리즘
# 수 묶기
# https://www.acmicpc.net/problem/1744

# 풀이
# 리스트를 0 이하, 1, 1 이상의 수의 리스트로 나누어
# 0 이하는 오름차순, 1 이상은 내림차순 정렬하고
# 앞에 수부터 두 개씩 묶어 더하여 최댓값을 구한다.
# 리스트의 length 가 홀수와 짝수일 때를 구분해야 한다.

# 마지막에 사용할 앞의 두 수씩 묶어 더하는 함수를 작성
def multi_sum(lst, answer):
    # 길이가 홀수일 때
    if len(lst) % 2 == 1:
        for x in range(len(lst) // 2):
            answer += (lst[2 * x] * lst[2 * x + 1])
        # 마지막에 남은 수를 더하기
        answer += lst[-1]
    # 길이가 짝수일 때
    else:
        for y in range(len(lst) // 2):
            answer += (lst[2 * y] * lst[2 * y + 1])
    return answer

# N을 입력받고 빈 리스트 생성
N = int(input())
array = []

# 입력값을 리스트로 받기
for i in range(N):
    array.append(int(input()))

# 구간별로 나누기 위해 오름차순 정렬
array.sort()

# 구간별 빈 리스트 생성
under_0 = []
over_1 = []
# 결과값을 넣을 result 를 0으로 초기화
result = 0

# 0 이하, 1, 1 이상의 수의 리스트로 나누기
for i in array:
    if i <= 0:
        under_0.append(i)
    # 1은 존재한다면 더해주는 것으로 처리
    elif i == 1:
        result += 1
    else:
        over_1.append(i)

# 1 이상의 수의 리스트를 내림차순으로 정렬
over_1.sort(reverse=True)

# 0 이하를 함수를 적용시켜 나온 값을 answer 로 하여 1 이상의 리스트와
# 함수를 한 번 더 적용
print(multi_sum(over_1, (multi_sum(under_0, result))))