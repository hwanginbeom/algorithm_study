def solution(s):
    def compression(size):
        before = s[:size]
        ret = 0
        count = 1
        for i in range(size, len(s), size):
            word = s[i : i+size]
            if word == before:
                count += 1
            else:
                if count > 1:
                    ret += len(str(count))
                ret += size
                before, count = word, 1
        if count > 1:
            ret += len(str(count))
        ret += len(before)
        return ret

    answer = len(s)
    for size in range(1, answer + 2 // 2):
        answer = min(answer, compression(size))
    return answer