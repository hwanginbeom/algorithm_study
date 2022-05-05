def solution(expression):
    operand = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '-', '+'), ('*', '+', '-')]
    answer = []
    for op in operand:
        a, b, _ = op
        temp_list = []
        for e in expression.split(a):
            temp = [f'({i})' for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)




expression = "100-200*300-500+20"
solution(expression)
