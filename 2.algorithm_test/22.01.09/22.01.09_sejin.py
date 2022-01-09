import re # 정규표현식 사용하기 위한 모듈

def solution(new_id) :

    # 1단계 : 모든 문자 소문자로 치환
    new_id = new_id.lower()
    # print(new_id)

    # 2단계 : 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # print(new_id)

    # 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub('\.{2,}', '.', new_id)
    # print(new_id)

    # 4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = re.sub('^\.|\.$', '', new_id)

    # 5단계 : 빈 문자열이라면, "a" 대입
    if len(new_id) == 0 :
        new_id = 'a'
    # print(new_id)

    # 6단계 : 길이가 16자 이상이면 처음 15자를 제외한 나머지 문자들이 제거
    #      : 제거 후 마침표(.)가 끝에 위치한다면 제거
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
        new_id = re.sub('\.$', '', new_id)
    # print(new_id)

    # 7단계 : 길이가 2자 이하라면 마지막 문자를 길이가 3될 때까지 붙인다
    if len(new_id) <= 2 :
        add = new_id[-1]
        while len(new_id) < 3:
            new_id += add
    # print(new_id)

    return(new_id)