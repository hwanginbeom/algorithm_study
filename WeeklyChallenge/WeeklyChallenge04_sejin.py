table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

def solution(table, languages, preference):
    new_table = [list(reversed(i.split(' '))) for i in table]

    check_lst = []
    for i in new_table:
        check = 0
        for x, y in zip(languages, preference):
            if x in i:
                check += (i.index(x)+1) * y
        check_lst.append(check)

    answer = new_table[check_lst.index(max(check_lst))][-1]
    return answer

print(solution(table, languages, preference))
