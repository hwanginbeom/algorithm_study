# 키패드 누르기
def path_calc(n, current):
    if n == 0: n = 11
    if current == 0: current = 11

    if n == current: return 0

    if current == '*' or current == '#':
        if n == 2: return 4
        if n == 5: return 3
        if n == 8: return 2
        if n == 11: return 1

    if current in [n - 1, n + 1, n - 3, n + 3]:
        return 1
    elif current in [n - 2, n + 2, n - 4, n + 4, n - 6, n + 6]:
        return 2
    elif current in [n - 5, n + 5, n - 7, n + 7, n - 9, n + 9]:
        return 3
    elif current in [n - 10, n - 8]:
        return 4


def solution1(numbers, hand):
    answer = ''

    current_L = '*'
    current_R = '#'

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            current_L = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            current_R = n
        else:
            path_L = path_calc(n, current_L)
            path_R = path_calc(n, current_R)

            if path_L < path_R:
                answer += 'L'
                current_L = n
            elif path_R < path_L:
                answer += 'R'
                current_R = n
            else:
                if hand == 'left':
                    answer += 'L'
                    current_L = n
                else:
                    answer += 'R'
                    current_R = n

    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
# print(solution1(numbers, hand))



# 순위 검색
from bisect import bisect_left

boolean_list = []
tmp = []


# 모든 경우의 수 True False 리스트 만들기
def sixteen():
    global boolean_list, tmp

    if len(tmp) == 4:
        t = []
        for index in tmp:
            t.append(index)
        boolean_list.append(t)

        return

    for i in (False, True):
        tmp.append(i)
        sixteen()
        tmp.pop()


def solution(info, query):
    global boolean_list

    answer = []
    dict = {}

    sixteen()

    # 지원자 분류
    for i in info :
        split_list = i.split(' ')
        score = int(split_list.pop())

        for j in range(len(boolean_list)) :
            temp = split_list.copy()

            for k in range(4) :
                if not boolean_list[j][k] :
                    temp[k] = '-'

            string = ''.join(temp)

            if string not in dict.keys() :
                dict[string] = [score]
            else :
                dict[string].append(score)

    # 계속 효율성 반만 맞았던 이유
    # 내장함수 sort도 시간복잡도를 차지하기 때문...
    # 검색 조건을 사용하는 반복문에서 sort를 쓰게 되면
    # 프로그램의 전체 시간복잡도가 늘어나는 것과 동일하므로 효율성은 낮아진다.
    # 반복문 바깥에서 전체를 정렬하는 것이 더 효율이 높다.
    for i in dict.keys() :
        dict[i].sort()

    # 검색 조건 사용
    for i in query :
        split_list = i.split(' ')
        score = int(split_list.pop())
        search = ''

        for j in split_list :
            if j != 'and' :
                search += j

        if search in dict.keys() :
            length = len(dict[search])

            # lower bound (bisect_left)
            index = bisect_left(dict[search], score)
            answer.append(length - index)
        else :
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
