import sys

input = sys.stdin.readline

eng_list = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def solution(s):
    answer = word = ''
    for text in s:
        if text.isdigit():
            answer += text
        else:
            word += text
            if word in eng_list.keys():
                answer += str(eng_list[word])
                word = ''
    return int(answer)

### replace로 구상했다가 안됐던 풀이
### 이렇게 하면 된다는걸 알아서 같이 작성
def solution(s):
    for idx, value in eng_list.items():
        s = s.replace(idx, str(value))
    return int(s)


s = "one4seveneight"
print(solution(s))
