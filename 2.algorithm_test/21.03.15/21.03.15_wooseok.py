# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065


def solution1(s):
    answer = []

    # 문자열 형태를 이중리스트 형식으로 변환
    s = s.strip('{')
    s = s.strip('}')
    str_split = s.split('},{')

    set_list = [[] for _ in range(len(str_split))]

    for i in range(len(str_split)):
        nums = str_split[i].split(',')
        set_list[i].extend(nums)

    # 정렬
    set_list = sorted(set_list, key=lambda x: len(x))

    # 튜플 만들기
    answer.append(int(set_list[0][0]))

    for i in range(1, len(set_list)):
        # 차집합
        temp = list(set(set_list[i]) - set(set_list[i - 1]))
        answer.append(int(temp[0]))

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution1(s))



# 오픈 채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution2(record):
    answer = []
    user_dic = {}

    # 유저 아이디와 닉네임 매칭
    for r in record:
        temp = r.split()

        if temp[0] != 'Leave':
            user_dic[temp[1]] = temp[2]

    # 딕셔너리에서 키를 이용하여 값을 찾아 넣기
    for r in record:
        temp = r.split()

        if temp[0] == 'Enter':
            answer.append(user_dic[temp[1]] + '님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(user_dic[temp[1]] + '님이 나갔습니다.')

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution2(record))
