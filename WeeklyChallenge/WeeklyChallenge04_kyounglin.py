# 2021-10-09

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/84325

# 위클리 챌린지 - 4주차_직업군 추천하기

#table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
#languages=["PYTHON", "C++", "SQL"]
#preference=[7, 5, 5]

table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages=["JAVA", "JAVASCRIPT"]
preference=[7, 5]

def solution(table, languages, preference):
    check_table = [list(reversed(i.split(' '))) for i in table]
    dict={}
    for i in check_table:
        score=0
        for la,pr in zip(languages,preference):
            if la in i:
                score+=(i.index(la)+1)*pr
        dict[i[-1]]=score

    answer=[key for key,value in dict.items() if value==max(dict.values())]

    return sorted(answer)[0]

print(solution(table, languages, preference))

