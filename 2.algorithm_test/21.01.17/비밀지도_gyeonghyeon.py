def solution(n, arr1, arr2):
    answer = [[] for _ in range(n)]
    as2 = []
    for idx, value in enumerate(zip(arr1,arr2)):
        arr1[idx] = format(value[0],'b').zfill(n)
        arr2[idx] = format(value[1], 'b').zfill(n)
    for idx2,value2 in enumerate(zip(arr1,arr2)):
        for idx3,value3 in enumerate(zip(value2[0],value2[1])):
            if value3[0] == '0' and value3[1] == '0':
                answer[idx2].append(' ')
            else:
                answer[idx2].append('#')
    for i in answer:
        as2.extend(''.join(i))
    res = []
    for ii in range(0,len(as2),n):
        res.append(''.join(as2[ii:ii+n]))
    return res
arr1 = 	[46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
solution(6, arr1, arr2)
