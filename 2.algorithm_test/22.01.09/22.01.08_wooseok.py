import re


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    temp = ''
    dot = ''
    for s in new_id:
        if s == '.':
            dot += s
        else:
            if dot:
                temp += '.' + s
                dot = ''
            else:
                temp += s

    new_id = temp

    while new_id and new_id[0] == '.':
        if new_id[0] == '.':
            new_id = new_id[1:]

    while new_id and new_id[-1] == '.':
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        rotateStr = new_id[-1]

        while len(new_id) < 3:
            new_id += rotateStr

    answer = new_id
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
