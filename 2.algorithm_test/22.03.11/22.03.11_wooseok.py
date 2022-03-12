# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []
    user_dict = {}

    for r in record:
        r_split = r.split()

        if r_split[0] == 'Enter':
            user_dict[r_split[1]] = r_split[2]
        elif r_split[0] == 'Change':
            user_dict[r_split[1]] = r_split[2]

    for r in record:
        r_split = r.split()

        if r_split[0] == 'Enter':
            answer.append(f'{user_dict[r_split[1]]}님이 들어왔습니다.')
        elif r_split[0] == 'Leave':
            answer.append(f'{user_dict[r_split[1]]}님이 나갔습니다.')

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
