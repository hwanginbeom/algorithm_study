def solution(numbers):
    answer = []
    for idx,i in enumerate(numbers):
        for idx2,k in enumerate(numbers):
            if idx == idx2:
                continue
            else:
                plus = i+k
                if plus not in answer:
                    answer.append(plus)
    return sorted(answer)

print(solution([2,1,3,4,1]))
