# 1
# 23분
def solution1(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 맞힌 문제 개수를 저장할 리스트 생성
    cnt = [0] * 3

    answer = []

    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            cnt[0] += 1

        if answers[i] == second[i % len(second)]:
            cnt[1] += 1

        if answers[i] == third[i % len(third)]:
            cnt[2] += 1

    maximum = max(cnt)

    for i in range(len(cnt)):
        if maximum == cnt[i]:
            answer.append(i + 1)

    return answer

answers = [1, 3, 2, 4, 2]
print(solution1(answers))


# 2
# 38분
def solution2(n, lost, reserve):
    answer = 0
    able_stu = n - len(lost)

    # 중복값 찾기
    overlap = list(set(lost).intersection(reserve))

    # 여벌 체육복을 가져온 학생이 도난당할 경우
    # 두 리스트에서 모두 지워준다.
    for i in range(len(overlap)):
        lost.remove(overlap[i])
        reserve.remove(overlap[i])
        able_stu += 1

    # 중복값 제거
    # 이 코드를 사용하면 테스트 하나 실패
    # for stu in lost :
    #     if stu in reserve :
    #         lost.remove(stu)
    #         reserve.remove(stu)
    #         able_stu += 1

    # 빌려줄 학생 찾기
    for stu in lost:
        if (stu - 1) in reserve:
            reserve.remove(stu - 1)
            able_stu += 1
            continue
        elif (stu + 1) in reserve:
            reserve.remove(stu + 1)
            able_stu += 1
            continue

    answer = able_stu
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution2(n, lost, reserve))


# 3
# 38분 (효율성 x)
def solution3(prices):
    answer = []
    cnt = 0

    while prices:
        price = prices.pop(0)

        for i in range(len(prices)):
            cnt += 1

            if price > prices[i]:
                break

        answer.append(cnt)
        cnt = 0

    return answer

prices = [1, 2, 3, 2, 3]
print(solution3(prices))
