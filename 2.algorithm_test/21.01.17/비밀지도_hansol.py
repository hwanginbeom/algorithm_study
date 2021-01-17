# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3#


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i]).lstrip('0b').zfill(n))

    for i in range(n):
        answer[i] = answer[i].replace('1', '#').replace('0', ' ')
    return answer


# 입출력 예제
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
