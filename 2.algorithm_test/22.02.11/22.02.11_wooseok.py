# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681


def make_zero(s, n):
    while len(s) < n:
        s = ''.join(['0', s])

    return s


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1_binary = format(arr1[i], 'b')
        arr2_binary = format(arr2[i], 'b')

        arr1_binary = make_zero(arr1_binary, n)
        arr2_binary = make_zero(arr2_binary, n)

        result_string = ''
        for j in range(n):
            result = int(arr1_binary[j]) or int(arr2_binary[j])
            if result:
                result_string += '#'
            else:
                result_string += ' '

        answer.append(result_string)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
