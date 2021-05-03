import itertools

def list_split(data):
    exp_list = []  # expression을 숫자와 연산기로 쪼개서 리스트
    oper_list = []  # 연산기 조합을 구하기 위해 연산기만 뽑은 리스트
    num = ''

    for i in range(len(data)):
        if i == len(data) - 1:
            num += data[i]
            exp_list.append(int(num))
        elif data[i].isdigit() == False:
            exp_list.append(int(num))
            exp_list.append(data[i])
            oper_list.append(data[i])
            num = ''
        else:
            num += data[i]
    return exp_list, oper_list


def cal_result(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def solution(expression):
    exp_list, oper = list_split(expression)
    oper_list = list(itertools.permutations(set(oper)))  # 연산기 조합 리스트

    max_val = 0
    value = 0

    for i in oper_list:
        a = exp_list.copy()

        for j in i:
            while True:
                try:
                    b = a.index(j)  # 특정 연산기 있는 인덱스 찾기
                    c = cal_result(a[b - 1], a[b + 1], j)  # 찾은 인덱스 앞 뒤 수 계산
                    del a[b - 1:b + 2]  # 연산기 위치, 앞 뒤 수 리스트에서 삭제
                    a.insert(b - 1, c)  # 지운 맨 앞자리에 계산한 수 넣기
                except ValueError:
                    break

        max_val = max(max_val, abs(a[0]))

    return max_val

expression = "100-200*300-500+20"
print(solution(expression))
