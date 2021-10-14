def solution(sizes):
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
    data = list(zip(*sizes))

    answer = max(data[0]) * max(data[1])
    return answer
