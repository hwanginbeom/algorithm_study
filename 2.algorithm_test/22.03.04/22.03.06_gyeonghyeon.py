def solution(s):
    answer = 1001
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        temp_str = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == temp_str:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp_str
                temp_str = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp_str
        answer = min(answer, len(result))
        result = ""

    return answer


s = "aabbaccc"
solution(s)
