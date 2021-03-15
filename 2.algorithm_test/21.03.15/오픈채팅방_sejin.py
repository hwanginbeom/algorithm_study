record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

info = dict()
answer = []


for j in record:
    data = j.split(' ')
    if data[0] != 'Leave':
        info[data[1]] = data[2]
# print(info)

for i in record:
    data = i.split(' ')

    if data[0] == 'Enter':
        answer.append(info[data[1]]+'님이 들어왔습니다.')
    elif data[0] == 'Leave':
        answer.append(info[data[1]] + '님이 나갔습니다.')
print(answer)
