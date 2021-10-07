def solution(table, languages, preference):
    job_score = {}
    pre_dict = {lang: pre for lang, pre in zip(languages, preference)}
    for i in table:
        score = i.split(' ')
        job_score[score[0]] = {values: 5 - idx for idx, values in enumerate(score[1:])}
    result = {}
    for job, num in job_score.items():
        temp = 0
        for idx, values in num.items():
            if idx in languages:
                temp += values * pre_dict[idx]
        result[job] = temp
    answer = sorted(result.items(), key = lambda item: (-item[1],item[0]))[0][0]
    return answer

