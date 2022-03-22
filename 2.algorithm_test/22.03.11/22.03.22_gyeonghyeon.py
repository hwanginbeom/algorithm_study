import sys

input = sys.stdin.readline


def solution(record):
    name_dic, answer = {}, []
    text_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for value in record:
        info = value.split(' ')
        if info[0] in ['Enter', 'Change']:
            name_dic[info[1]] = info[2]

    for text in record:
        info_1 = text.split(' ')
        if info_1[0] != 'Change':
            answer.append(f'{name_dic[info_1[1]]}{text_dict[info_1[0]]}')
    return answer
