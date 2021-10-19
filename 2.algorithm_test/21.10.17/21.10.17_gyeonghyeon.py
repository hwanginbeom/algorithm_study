from itertools import combinations


def solution(info, query):
    answer = []
    db = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            print(combi)
            for c in combi:
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():
        value.sort()

    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
solution(info, query)