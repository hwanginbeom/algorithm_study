def solution(lines):
    logs = []

    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(':')
        end = (int(h)*60*60 + int(m)*60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end))

    length = len(logs)
    max_ = 1

    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            if logs[j][1] - logs[i][1] >= 4000:
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_ = max(max_, cnt)

    return max_
