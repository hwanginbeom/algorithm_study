# 아이디어 구상
# 앞에가 있고, 뒤에가 없어
# 	=> 앞+뒤 append
# 	=> 앞 값 출력
#
# 앞에가 있고, 뒤에도 있어
# 	=> 뒤 값을 +1
# 결국엔, 뒤에가 없을 때까지
# 	=> 앞+뒤 append
# 	=> 앞 값 출력

def solution(msg):

    dict = {} # 기본 A~Z 리스트
    for i in range(65, 91):
        dict[chr(i)] = i - 64

    answer = []
    i = 0
    while (i < len(msg)):
        j = 1

        while (i+j+1 <= len(msg)) and (msg[i:i+j+1] in dict):
            j += 1

        answer.append(dict[msg[i:i+j]])
        dict[msg[i:i+j+1]] = max(dict.values()) + 1
        i += j

    return answer
