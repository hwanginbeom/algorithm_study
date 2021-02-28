# 2021-02-28

# 신규 아이디 추천

# 예시1
new_id="=.="

import re

def solution(new_id):
    # 단계1(소문자 변경)
    # 단계2(정규표현식으로 특수문자확인 및 제거)
    new_id=re.sub("[^a-z\d\_\-\.]", "", new_id.lower())
    # 단계3(연속 . 제거)
    new_id=re.sub('\.\.+','.',new_id)
    # 단계4(마침표가 처음이나 끝에 위차한다면 제거)
    if len(new_id)>0:
        if new_id[0]=='.':
            new_id=new_id[1:]
    if len(new_id)>0:
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    # 단계5(new_id가 빈 문자열이라면, new_id에 "a"를 대입)
    if new_id=='':
        new_id='a'
    # 단계6(아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거/ 마지막. 제거)
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    # 단계7( new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복)
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

print(solution(new_id))