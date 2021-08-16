# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 21.03.15 재풀이


def solution(record) :
    answer = []
    user_dict = {}

    for r in record :
        split_list = r.split()

        if split_list[0] != 'Leave' :
            user_dict[split_list[1]] = split_list[2]

    for r in record :
        split_list = r.split()

        if split_list[0] == 'Enter' :
            message = user_dict[split_list[1]] + '님이 들어왔습니다.'
            answer.append(message)
        elif split_list[0] == 'Leave' :
            message = user_dict[split_list[1]] + '님이 나갔습니다.'
            answer.append(message)

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
