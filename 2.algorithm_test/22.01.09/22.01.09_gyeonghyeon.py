import re

def solution(new_id):
    new_id = ''.join([ i.lower() for i in list(new_id)])
    new_id = ''.join(re.findall(r'[0-9 | a-z | \- | \_ | \.]', new_id))
    new_id = re.sub('[..]+', ".", new_id)
    if new_id[0] == ".":
        if len(new_id) > 1:
            new_id = new_id[1:]
        else:
            new_id = "a"
    if new_id[-1] == ".":
        if len(new_id) > 1:
            new_id = new_id[:-1]
        else:
            new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) < 3:
        new_id = new_id.ljust(3, new_id[-1])
    answer = new_id
    return answer


