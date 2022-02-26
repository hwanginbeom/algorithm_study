# 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {}

    # 딕셔너리 아이디 순서 지정
    for i in id_list :
        report_dict[i] = set([])

    # 유저마다 신고한 유저 저장
    for s in report:
        report_user, reported_user = s.split()
        report_dict[report_user].add(reported_user)

    # 유저의 신고당한 횟수 생성
    reported_user_dict = {}
    for value in report_dict.values():
        for i in value:
            if i in reported_user_dict.keys():
                reported_user_dict[i] += 1
            else:
                reported_user_dict[i] = 1

    # 특정 횟수보다 많이 신고받은 유저를 신고한 유저 메일 수 결과 세기
    idx = 0
    for value in report_dict.values():
        for i in value:
            if reported_user_dict[i] >= k :
                answer[idx] += 1

        idx += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))
