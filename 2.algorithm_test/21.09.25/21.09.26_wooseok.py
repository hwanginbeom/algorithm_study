# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
# 21.03.15 재풀이

# 문자열 입력을 리스트로 변환하는 함수 - 스택 활용
def string_to_list(s):
    stack = []
    tuple_list = []
    num_str = ''

    for i in s:
        if i.isdigit():
            num_str += i
        elif i == ',':
            stack.append(num_str)
            num_str = ''
        elif i == '}':
            stack.append(num_str)
            num_str = ''

            temp = []
            while stack[-1].isdigit():
                num = int(stack.pop())
                temp.append(num)

            temp = temp[::-1]
            tuple_list.append(temp)
        else:
            stack.append(i)

    return tuple_list[:-1]


def solution(s):
    answer = []

    tuple_list = string_to_list(s)
    sorted_list = sorted(tuple_list, key=lambda x: len(x))
    # print(sorted_list)

    for s in sorted_list:
        rest = set(s) - set(answer) # 차집합 사용
        answer.extend(list(rest))

    return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))
# 성공
