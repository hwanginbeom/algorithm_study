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


def solution(numbers, hand):
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
print(solution(numbers, hand))



# 순위 검색
import re


def solution(info, query):
    answer = []

    for q in query:
        score = re.findall('\d+', q)
        q_words = q.split('and')
        print(q_words)

        for i in info:
            i_words = i.split(' ')
            print(i_words)

            for j in q_words:
                j = re.findall('\D+', j)
                j = j[0].strip()

                for k in i_words:
                    k = k.strip()

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
