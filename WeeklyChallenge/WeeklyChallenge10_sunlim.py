#10. 교점에 별만들기

def solution(line):
    answer = []
    result = []

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            s = solve(line[i], line[j])

            if s != None:
                r1 = min(r1, s[1]) if len(result) != 0 else s[1]
                r2 = max(r2, s[1]) if len(result) != 0 else s[1]
                c1 = min(c1, s[0]) if len(result) != 0 else s[0]
                c2 = max(c2, s[0]) if len(result) != 0 else s[0]
                result.append(s)

    answer = [['.'] * (c2 - c1 + 1) for i in range(r2 - r1 + 1)]

    for x, y in result:
        answer[y - r1][x - c1] = '*'

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer


def solve(eq1, eq2):
    A, B, E = eq1
    C, D, F = eq2

    if A * D - B * C != 0 and (B * F - E * D) % (A * D - B * C) == 0 and (E * C - A * F) % (A * D - B * C) == 0:
        return [(B * F - E * D) // (A * D - B * C), - (E * C - A * F) // (A * D - B * C)]
    else:
        return None


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8,
                                                                    12]]))  # ['....*....', '.........', '.........', '*.......*', '.........', '.........', '.........', '.........', '*.......*']