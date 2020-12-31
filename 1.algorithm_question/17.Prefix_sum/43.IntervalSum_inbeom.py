def solution(numbers):
    answer=[]
    for i in range(0,len(numbers)):
        for j in range(1+i,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    # print(answer)
    return answer

numbers = [2,1,3,4,1]
numbers = [5,0,2,7]
solution(numbers)