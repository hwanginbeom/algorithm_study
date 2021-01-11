def solution(N, stages):
    answer = []

    n = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        # print(count)

        if count == 0:
            percentage = 0
        else:
            percentage = count / n
            # print(percentage)

        answer.append((i, percentage))
        n -= count

    # print(answer)
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    # print(answer)
    return ( [y for x, y in answer] )


print(solution(4, [4,4,4,4,4]))
