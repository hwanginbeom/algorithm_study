def solution(table, languages, preference):
    answer = []   #여기에 값넣어야해
    new_table = sorted([list(t.split()) for t in table], key=lambda x : x[0])
    job = {n: new_table[n][0] for n in range(len(new_table))}

    for j in range(len(job)):    #for구문 중요!! 혼자 만들수 있는 스킬늘리기!!!!
        total = 0
        for lang, pref in zip(languages, preference):
            if lang in new_table[j]:
                total += (6 - new_table[j].index(lang)) * pref
        answer.append(total)

    return job[answer.index(max(answer))]