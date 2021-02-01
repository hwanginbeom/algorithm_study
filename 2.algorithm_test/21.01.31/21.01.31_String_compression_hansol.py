# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


s = input()

def solution(s):
    answer = 1000000
    check_list = []
    check = []
    for cut in range(1, len(s) // 2 + 2): # 여기서 2는 문자열이 한자리인 경우
        slice = s[0:cut]
        count = 1
        result = ''
        for j in range(cut, len(s) + cut, cut): # 문자열이 1이면 cut도 1 for문 1,1,1은 말이 안됨. 그러므로 cut만큼 더 더해주어야 함
            if slice == s[j:j + cut]:
                count += 1
            else:
                if count == 1:
                    result += slice
                else:
                    result += str(count) + slice
                slice = s[j:cut + j]
                count = 1
        answer = min(answer, len(result))

    return answer

print(solution(s))