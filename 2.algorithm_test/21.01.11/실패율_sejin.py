# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []

    n = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)

        if count == 0:
            percentage = 0
        else:
            percentage = count / n

        answer.append((i, percentage))
        n -= count

    # print(answer)
    answer = sorted(answer, key = lambda x : x[1], reverse=True)
    return ( [x for x, y in answer] )

print(solution(4, [4,4,4,4,4]))
