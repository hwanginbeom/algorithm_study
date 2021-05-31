# n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687


def convert(n, base):
    arr = "0123456789ABCDEF"

    # divmod(a, b) : a를 b로 나눈 몫과 나머지를 반환
    q, r = divmod(n, base)

    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    string = ''

    for i in range(t * m):
        string += convert(i, n)

    # print(string)

    while True:
        answer += string[p - 1]
        p += m

        if len(answer) == t:
            break

    return answer


n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))
