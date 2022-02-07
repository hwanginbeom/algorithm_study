def solution(board, moves):
    stack = []
    answer = 0
    for x in moves:
        for y in board:
            if y[x-1] != 0:
                stack.append(y[x-1])
                y[x-1] = 0
                break
            else:
                continue
        if len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
            answer += 1
    return answer * 2