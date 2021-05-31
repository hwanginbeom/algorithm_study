def solution(n, t, m, p):

    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    answer = ''
    candidate = []

    for i in range(t*m):
        conv = convert(i, n)
        for c in conv:
            candidate.append(c)

    for i in range(p-1, t*m, m):
        answer += candidate[i]

    return answer