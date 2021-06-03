# 중량제한
# https://www.acmicpc.net/problem/1939


def solution() :
    n, m = map(int, input().split())

    know_true_list = list(map(int, input().split()))
    know_true_list = know_true_list[1:]

    party_list = []
    for _ in range(m) :
        temp = list(map(int, input().split()))
        temp = temp[1:]

        party_list.append(temp)

    know_true_set = set(know_true_list)

    # 과장된 말을 할 수 있는 파티이면 1, 아니면 0
    count_list = [1] * m

    for _ in range(m) :
        for idx, _list in enumerate(party_list) :
            list_set = set(_list)

            # 모든 파티를 돌면서 겹치는 사람이 있는지 검사
            if know_true_set.intersection(list_set) :
                know_true_set = know_true_set.union(list_set)
                count_list[idx] = 0

    print(sum(count_list))


solution()
