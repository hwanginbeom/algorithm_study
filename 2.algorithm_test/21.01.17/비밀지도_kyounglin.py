# 비밀지도

# 2021-01-17

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    check=[]
    answer=[]

    for i in range(n):
        check.append(bin(arr1[i]|arr2[i])[2:].zfill(n))

    for j in range(len(check)):
        answer.append(check[j].replace("1","#").replace("0"," "))

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

