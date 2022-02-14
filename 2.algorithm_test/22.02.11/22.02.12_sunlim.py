def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # tmp결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n)
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1', '#').replace('0', ' ')
        # tmp결과 ex) ' ## #'
        answer.append(tmp)

    return answer