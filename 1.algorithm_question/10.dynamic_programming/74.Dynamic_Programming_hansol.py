# 계단 오르기
# Dynamic Programming
# https://www.acmicpc.net/problem/2579

n = int(input())
# 입력값을 score 리스트에 저장
score = []
for _ in range(n):
    score.append(int(input()))

# result 초기값을 충분한 길이로 설정
result = [0] * 301

def max_score(x):
    # 시작점, 첫번째, 두번째 계단의 결과값을 저장
    if x == 0: return 0
    elif x == 1: return score[0]
    elif x == 2: return score[0] + score[1]
    # 값이 설정되면 저장하는 다이나믹 프로그래밍 활용
    if result[x] != 0:
        return result[x]
    # x-1 번째 계단을 거치는 것과 건너뛰는 경우 중 큰 값을 반환하는 점화식
    result[x] = max(score[x - 1] + score[x - 2] + max_score(x - 3),
                    score[x - 1] + max_score(x - 2))
    return result[x]

print(max_score(n))