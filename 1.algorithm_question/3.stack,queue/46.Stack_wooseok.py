# 괄호
def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        ps = list(input())
        stack = []

        for _ in range(len(ps)) :
            # 괄호문자열의 맨 뒤 부터 하나씩 뽑아내기
            p = ps.pop()

            # 스택 리스트에 추가
            stack.append(p)

            # 스택에 문자가 2개 이상일 경우
            if len(stack) >= 2 :
                # 스택의 상위 두 문자를 꺼내고
                p1 = stack.pop()
                p2 = stack.pop()

                # 유효한 괄호문자열인지 확인
                if p1 == '(' and p2 == ')' :
                    continue
                else :
                    stack.append(p2)
                    stack.append(p1)

        if stack :
            answer.append('NO')
        else :
            answer.append('YES')

    for i in answer :
        print(i)


solution()
