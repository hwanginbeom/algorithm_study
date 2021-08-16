record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

info = dict()
answer = []

# info 딕셔너리에 아이디별 닉네임 먼저 다 생성해주기
for i in record:
    data = i.split(' ')
    if data[0] != 'Leave':
        info[data[1]] = data[2]

for j in record:
    data = j.split(' ')

    if data[0] == 'Enter':
        answer.append('{}님이 들어왔습니다.'.format(info[data[1]]))
    elif data[0] == 'Leave':
        answer.append('{}님이 나갔습니다.'.format(info[data[1]]))
print(answer)
