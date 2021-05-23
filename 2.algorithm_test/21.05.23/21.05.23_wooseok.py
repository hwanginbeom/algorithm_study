# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684


# 리스트에서 가장 긴 단어의 길이를 반환
def findMaxLength(_list):
    temp = []

    for i in _list:
        temp.append(len(i))

    return max(temp)


def solution(msg):
    answer = []
    _dict = {}

    # 길이가 1인 모든 단어 사전 생성
    for i in range(65, 91):
        _dict[chr(i)] = i - 64

    max_value = 26

    while True:
        key_list = list(_dict.keys())
        max_length = findMaxLength(key_list)

        # 사전에서 제일 긴 단어의 길이부터 확인해나가기
        for i in range(max_length, 0, -1):
            w = msg[:i]

            # 사전에 있으면 값 추가
            if w in key_list:
                answer.append(_dict[w])
                max_value += 1

                # 사전에 새로운 단어 추가
                if i < len(msg) :
                    c = msg[i]
                    _dict[w + c] = max_value

                # 다음 문자열로 갱신
                msg = msg[i:]

                break

        if not msg :
            break

    return answer


msg = 'KAKAO'
print(solution(msg))
