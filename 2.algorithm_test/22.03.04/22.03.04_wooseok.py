# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = 0
    total_list = []

    # 문자열을 문자 하나씩 나누기, 두개씩 나누기, 세개씩 나누기 ...
    for i in range(1, len(s) // 2 + 1):
        count = 1
        total = 0
        temp = 0
        str_count = []

        string = s[:i]

        # 겹치는 문자의 개수 찾기
        for j in range(i, len(s), i):
            if string == s[j:j + i]:
                count += 1
            else:
                if count > 1:
                    str_count.append({string: count})
                    count = 1

                string = s[j:j + i]
        if count > 1:
            str_count.append({string: count})

        # 겹쳐지지 않는 남는 문자 개수 찾기
        for d in str_count:
            for key, value in d.items():
                total += len(key) + len(str(value))
                temp += len(key) * value

        total += len(s) - temp
        total_list.append(total)

    # 문자열의 길이가 0인 경우 찾기
    if total_list :
        answer = min(total_list)
    else :
        answer = len(s)

    return answer


s = "aabbaccc"
print(solution(s))
