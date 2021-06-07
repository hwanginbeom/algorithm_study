# 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676


def check(time, _list):
    num = 0

    start = time
    end = time + 1000

    for i in _list:
        if not (i[1] < start or i[0] >= end):
            num += 1

    return num


def solution(lines):
    answer = 0

    time_list = []

    for line in lines:
        split_list = line.split()
        time_split = split_list[1].split(':')

        hour_to_second = int(time_split[0]) * 3600
        minute_to_second = int(time_split[1]) * 60
        second = (float(time_split[2]) + hour_to_second + minute_to_second) * 1000
        pre_second = second - float(split_list[2].replace('s', '')) * 1000 + 1

        time_list.append([pre_second, second])

    # print(time_list)
    max_count = 0

    for time in time_list:
        max_count = max(max_count, check(time[0], time_list), check(time[1], time_list))

    answer = max_count

    return answer


lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
