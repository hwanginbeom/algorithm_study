def solution(id_list, report, k):
    get_report = {name: [set({}), 0] for name in id_list}  # 누구에게 신고 받았는지
    reported = {name: set({}) for name in id_list}  # 누구를 신고했는지
    for content in report:
        user, get_user = content.split(' ')  # 신고한 사람, 신고 받은 사람
        user_list = get_report.get(get_user)  # 신고 받은 사람 dict에서 신고한 사람 리스트
        if user not in user_list[0]:
            get_report[get_user][0].add(user)  # 신고한 사람이 없었다면 추가하기
            get_report[get_user][1] += 1
        reported[user].add(get_user)  # 내가 신고한 사람 추가
    get_report = dict(sorted(get_report.items(), key=lambda x: x[1][1], reverse=True))
    get_user_list = set([name for name, value in get_report.items() if k <= value[1]])
    answer = []
    for name, value in reported.items():
        answer.append(len(value & get_user_list))
    print(answer)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
solution(id_list, report, k)
