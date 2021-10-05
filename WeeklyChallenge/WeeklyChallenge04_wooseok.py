# 직업군 추천하기
# https://programmers.co.kr/learn/courses/30/lessons/84325


def solution(table, languages, preference):
    answer = ''

    prefer_language_dict = {}
    total_score_dict = {}

    # 선호 언어와 점수 결합
    for i in range(len(languages)):
        prefer_language_dict[languages[i]] = preference[i]

    for i in range(len(table)):
        split_list = table[i].split()
        job = split_list[0]
        score_list = split_list[1:]

        table_score_dict = {}

        # 직업군별 언어와 점수를 결합
        for j in range(len(score_list)):
            table_score_dict[score_list[j]] = 5 - j

        total_score = 0

        # 직업군의 언어중에 선호 언어가 있는지 확인 후 점수 계산
        for key in prefer_language_dict.keys():
            if key in table_score_dict.keys():
                total_score += table_score_dict[key] * prefer_language_dict[key]

        total_score_dict[job] = total_score

    sorted_list = sorted(total_score_dict.items(), key=lambda x: (-x[1], x[0]))
    answer = sorted_list[0][0]

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, languages, preference))
