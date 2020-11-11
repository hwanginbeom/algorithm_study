# 1
def solution1() :
    n = int(input())

    rope_list = []
    for _ in range(n) :
        rope_list.append(int(input()))

    # 로프가 견딜 수 있는 하중 리스트를 내림차순으로 정렬
    rope_list.sort(reverse = True)
    weight_list = [rope_list[0]]

    # 무거운 중량을 들 수 있는 로프부터 앞에서 1개, 2개, 3개 ... 순으로 가능한 중량의 합 계산
    for i in range(1, n) :
        weight_list.append(rope_list[i] * (i + 1))

    print(max(weight_list))


# solution1()



# 2
def solution2() :
    n = int(input())

    conf_info = []

    for _ in range(n) :
        start_time, end_time = map(int, input().split())

        conf_info.append([start_time, end_time])

    # 시작 시간 기준으로 정렬한 후 종료시간 기준으로 정렬
    # 종료 시간 기준으로만 정렬을 한 결과와 다르다.
    conf_info = sorted(conf_info, key = lambda x : x[0])
    conf_info = sorted(conf_info, key = lambda x : x[1])

    # 이전 회의(첫 회의)의 종료 시간
    end = conf_info[0][1]
    cnt = 1

    # 이전 회의의 종료 시간이 다음 회의의 시작 시간보다 같거나 작으면 count 1 증가
    for i in range(1, len(conf_info)) :
        temp_start = conf_info[i][0]
        temp_end = conf_info[i][1]

        if end <= temp_start :
            end = temp_end
            cnt += 1

    print(cnt)


# solution2()
