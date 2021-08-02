import re
def solution(files):
    file2 = [ re.split(r'([0-9]+)', i) + [idx] for idx,i in enumerate(files)]
    answer = [''.join(i[0:-1]) for i in sorted(file2, key=lambda x:(x[0].lower(),int(x[1]),x[-1]))]
    print(answer)
    return answer
solution(["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])