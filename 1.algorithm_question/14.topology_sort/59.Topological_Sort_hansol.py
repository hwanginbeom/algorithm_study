# 8. 기타 그래프 이론
# 위상 정렬
# 게임 개발
# https://www.acmicpc.net/problem/1516

def solution(lists):
    answer = [0] * len(lists)
    # 먼저 짓는 것이 없는 경우
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            answer[i] = lists[i][0]
    while 0 in answer:
        for i in range(len(lists)):
            buildtime = lists[i][0]
            buildtimes = list()
            if answer[i] != 0:
                continue
            else:
                for j in range(1, len(lists[i])):
                    if j == len(lists[i]) - 1:
                        answer[i] = max(buildtimes)
                    else:
                        if answer[lists[i][j] - 1] != 0:
                            buildtimes.append(buildtime + answer[lists[i][j] - 1])
                        else:
                            break
    return answer

def main():
    n = int(input())
    lists = list()
    for i in range(n):
        build = list(map(int, input().split()))
        lists.append(build)

    answer = solution(lists)
    for i in answer:
        print(i)

main()