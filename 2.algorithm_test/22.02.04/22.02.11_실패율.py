import sys

input = sys.stdin.readline


def solution(N, stages):
    stage_list = []
    stages.sort()
    if stages[-1] <= N:
        m = N
    else:
        m = stages[-1]
    for i in range(m):
        stage_cnt = stages.count(i + 1)
        if stage_cnt is not None:
            stage_list.append(stage_cnt)
        else:
            stage_list.append(0)
    answer = [[i+1] for i in range(N)]
    for i in range(N):
        try:
            h = stage_list[i] / sum(stage_list[i:])
            answer[i].append(1 - h)
        except ZeroDivisionError:
            answer[i].append(1)
    answer = [i[0] for i in sorted(answer, key=lambda x:(x[1], x[0]))]
    return answer
