n = 6
arr1 =[46,33,33,22,31,50]
arr2 =[27,56,19,14,14,10]

def change(x) :
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
        a1.append(change(arr1[i]))
    a2 = []
    for i in range(len(arr2)) :
        a2.append(change(arr2[i]))

    answer = []
    for j in range(n) :
        result = []
        for k in range(n) :
            if (a1[j][k] == "0") and (a2[j][k] == "0") :
                result.append(" ")
            else :
                result.append("#")
        answer.append(''.join(result))
    return(answer)

print(solution(n,arr1,arr2))