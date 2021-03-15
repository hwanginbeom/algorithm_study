# 2021-03-15

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42888

# 오픈채팅방

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    check=[]
    id={} # id와 nick_name을 담을 딕셔너리

    for i in record:
        array=i.split() # 공백을 기준으로 split
        if array[0]=='Leave': # check라는 리스트에 [id,액션] 담아 leave면 나갔습니다. 라고 액션
            check.append([array[1],"님이 나갔습니다."])
        elif array[0]=='Enter':
            id[array[1]]=array[2] # id딕셔너리(key=id) -> 값은 닉네임으로 id 넣기
            check.append([array[1],"님이 들어왔습니다."]) # [id,액션] 담기
        else: # change면 딕셔너리 id(key값)을 새로운 닉네임으로 변경
            id[array[1]]=array[2]

    answer=[]
    for j in check:
        answer.append(id[j[0]]+j[1]) # 문자끼리는 결합이 가능. 이때 j[0]=> check의 아이디 값으로 딕셔너리의 value찾기
    return answer
