# https://programmers.co.kr/learn/courses/30/lessons/17681

def change(n, x) :
    y = ""
    while x > 0 :
        div = x // 2
        mod = x % 2
        x = div
        y += str(mod)
    return y[::-1].zfill(n)

def solution(n, arr1, arr2) :
    a1 = []
    for i in range(len(arr1)) :
        a1.append(change(n, arr1[i]))
    a2 = []
    for i in range(len(arr2)) :
        a2.append(change(n, arr2[i]))

    answer = []
    for j in range(n) :
        result = []
        for k in range(n) :
            if (a1[j][k] == "0") and (a2[j][k] == "0") :
                result.append(" ")
            else :
                result.append("#")
        answer.append(''.join(result))
    return answer

print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))


# 경린언니 숏 코딩
#
# def solution(n, arr1, arr2) :
#
#     change = []
#     answer = []
#
#     for i in range(n) :
#         # bin(number), format(number, 'b') : 정수를 이진수 문자열로 바꾸는 함수
#         change.append(bin(arr1[i]|arr2[i])[2:].zfill(n))
#
#     for j in range(len(change)):
#         answer.append(change[j].replace("0"," ").replace("1","#"))
#
#     return answer