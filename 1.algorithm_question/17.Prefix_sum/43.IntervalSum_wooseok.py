# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    l = len(numbers)

    for i in range(l):
        for j in range(i + 1, l):
            num = numbers[i] + numbers[j]

            if num not in answer:
                answer.append(num)

    answer.sort()

    return answer


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
