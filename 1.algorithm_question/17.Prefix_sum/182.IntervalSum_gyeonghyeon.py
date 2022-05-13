def solution():
    answer = 0
    for _ in range(10):
        score = int(input())
        answer += score
        if answer >= 100:
            prev, nxt = 100 - (answer - score), abs(answer - 100)
            if prev < nxt:
                answer -= score
                return answer
            elif nxt < prev or prev == nxt:
                return answer
    return answer


print(solution())
