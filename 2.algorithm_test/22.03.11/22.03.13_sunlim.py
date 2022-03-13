#프로그래머스 오픈채팅방


def solution(record):
    answer = []
    users = {}  #유저 아이디 딕셔너리
    log = []
    for r in record:   #반복문을 통해 각 레코드에 대해 조건문 실행!
        part = r.split(" ")
        uid = part[1]
        if part[0] == "Enter":
            log.append((uid, "E"))
            users[uid] = part[2]
        elif part[0] == "Leave":
            log.append((uid, "L"))
        else:
            log.append((uid, "C"))
            users[uid] = part[2]

    for l in log:
        if l[1] == "E":
            answer.append(users[l[0]]+"님이 들어왔습니다.")
        elif l[1] == "L":
            answer.append(users[l[0]]+"님이 나갔습니다.")

    return answer
