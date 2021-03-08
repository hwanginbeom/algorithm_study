answer = 0

def dfs(numbers, target, length, i):
    if i == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        dfs(numbers, target, length, i+1)
        numbers[i] *= -1
        dfs(numbers, target, length, i+1)

def recursive_solution(numbers, target):
    length = len(numbers)
    dfs(numbers, target, length, 0)

    return answer
