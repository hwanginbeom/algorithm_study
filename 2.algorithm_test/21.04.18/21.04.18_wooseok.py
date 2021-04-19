# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058


# 균형잡힌 괄호 문자열인지 검사하는 함수
def isBalance(_list):
    left = _list.count('(')
    right = _list.count(')')

    if left == right:
        return True
    else:
        return False


# 올바른 괄호 문자열인지 검사하는 함수
def isCorrect(string):
    stack = []
    str_list = list(string)

    for i in str_list:
        stack.append(i)

        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    # 1 단계
    if not p :
        return ''
    else :
        temp_list = []
        u = ''
        v = ''

        # 2 단계
        for i in range(len(p)):
            temp_list.append(p[i])

            if isBalance(temp_list):
                u = ''.join(temp_list)
                v = p[(i + 1):]
                break

        # 3 단계
        if isCorrect(u):
            # 3-1 단계
            return u + solution(v)
        else:
            # 4-1 단계
            answer = '('

            # 4-2 단계
            answer += solution(v)

            # 4-3 단계
            answer += ')'

            # 4-4 단계
            for i in range(1, len(u) - 1) :
                if u[i] == '(' :
                    answer += ')'
                else :
                    answer += '('

            # 4-5 단계
            return answer


p = "(()())()"
print(solution(p))

# 1단계 부터 다시 수행하라는 것은 그냥 solution() 함수를 재귀하면 되는거였다...
