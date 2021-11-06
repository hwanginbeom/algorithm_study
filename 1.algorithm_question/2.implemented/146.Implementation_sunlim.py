#백준 8958번

n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커짐
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)