# 2021-01-19

# 파일명 정렬

# https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):

# () 사용하면 해당 분리 문자도 결과에 표현 --> 숫자 기준으로 split
    check=[re.split('(\d+)',value) for value in files]
# 정렬
    sort=sorted(check,key=lambda x : (x[0].lower(),int(x[1])))
    answer=[''.join(i) for i in sort]
    return answer


# 예시 답안
print(solution(['img12.png','img10.png','img02.png','img1.png','IMG01.GIF','img2.JPG']))
print(solution(['F-5 Freedom Fighter','B-50 Superfortress','A-10 Thunderbolt II','F-14 Tomcat']))
