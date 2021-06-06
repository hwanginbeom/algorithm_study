def solution(lines):
    answer = 0
    log = []
    for line in lines:
        s, t = list(map(lambda x : x.split(':') if 's' not in x else x.replace('s', ''), line.split()[1:]))
        end = (int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])) * 1000
        start = end - float(t) * 1000 + 1
        log.append([start, end])
    for x in log:
        answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))
    return answer


def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt


lines = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
solution(lines)
