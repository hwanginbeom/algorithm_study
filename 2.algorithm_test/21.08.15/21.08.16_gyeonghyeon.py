import sys
input = sys.stdin.readline


def solution(record):
    name_dic, answer = {}, []
    for value in record:
        info = value.split(' ')
        if info[0] == 'Enter':
                name_dic[info[1]] = info[2]
        elif info[0] == 'Change':
            name_dic[info[1]] = info[2]

    for text in record:
        info_1 = text.split(' ')
        if info_1[0] == 'Enter':
            answer.append(f'{name_dic[info_1[1]]}님이 들어왔습니다.')
        elif info_1[0] == 'Leave':
            answer.append(f'{name_dic[info_1[1]]}님이 나갔습니다.')
    return answer