# 신입 사원
# https://www.acmicpc.net/problem/1946


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())

        applicant_list = []
        for _ in range(n) :
            _set = tuple(map(int, input().split()))
            applicant_list.append(_set)

        applicant_list.sort()
        count = 0
        _min = 100001

        # 서류 순위대로 먼저 오름차순 정렬을 한 이후
        # 서류와 면접 순위 둘 다 어떤 지원자보다 낮으면 떨어지므로
        # 서류 순위가 낮은 지원자의 면접 순위가
        # 서류 순위가 높은 지원자들의 면접 순위보다 높기만 하면 선발이 된다.
        # 반복을 하면서 높은 면접 순위를 계속 갱신한다. (시간초과 해결)
        for i in range(len(applicant_list)) :
            if _min > applicant_list[i][1] :
                _min = applicant_list[i][1]
                count += 1

        answer.append(count)

    for i in answer :
        print(i)


solution()
