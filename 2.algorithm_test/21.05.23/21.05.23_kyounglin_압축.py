# 2021-05-26

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17684

# 압축

msg = 'KAKAO'
# msg='TOBEORNOTTOBEORTOBEORNOT'
# msg='ABABABABABABABAB'


def solution(msg):
    dict = {}

    # 알파벳 사전만들기
    for i in range(65, 91):
        dict[chr(i)] = i - 64

    start, end = 0, len(msg)
    answer = []

    while True:
        if msg[start:end] in dict.keys():
            answer.append(dict[msg[start:end]])  # 사전 번호 넣기

            if end == len(msg):  # 마지막 위치의 단어일때 알고리즘 종료
                return answer  # 사전번호 출력
                break

            # 새로운 단어 사전 입력
            dict[msg[start:end] + msg[end]] = max(dict.values()) + 1
            start += len(msg[start:end])  # 다음단어로 이동
            end = len(msg)  # 끝값은 처음위치로 돌려야함

        else:
            end -= 1

print(solution(msg))