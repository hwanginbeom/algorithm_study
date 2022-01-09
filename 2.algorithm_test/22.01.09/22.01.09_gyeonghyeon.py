import re

def solution(new_id):
    data1 = new_id.lower()
    data2 = re.sub('[^a-z0-9\-\_\.]', '', data1)  #re.findall(r'[0-9 | a-z | \- | \_ | \.]', new_id)
    new_id = re.sub('[..]+', '.', data2)

    if len(new_id) >= 1:
        if new_id[0] == '.':
            new_id = new_id[1:]

    if len(new_id) >= 1:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif len(new_id) <= 2:  #new_id.ljust(3, new_id[-1])
        while (len(new_id) < 3):
            new_id += new_id[-1]

    return (new_id)
