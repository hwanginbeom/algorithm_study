def solution(msg):
    str_list = {chr(x) : x-64 for x in range(65, 91)}
    answer = []
    start, end = 0, len(msg)
    while True:
        a = msg[start:end]
        if a in str_list.keys():
            answer.append(str_list[a])
            if end >= len(msg):
                return answer
            str_list[a + msg[end]] = max(str_list.values()) + 1
            start += len(a)
            end = len(msg)
        else:
            end -= 1

msg = 'KAKAO'
solution(msg)