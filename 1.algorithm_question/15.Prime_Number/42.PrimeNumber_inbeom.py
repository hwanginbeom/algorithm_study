
while(1):
    K, M, P = map(int, input().split())
    if K == 0 and M == 0 and P == 0:
        break
    array=[]
    array.append(K)
    array.append(M)
    array.append(P)
    array.sort()
    b = array[-1] ** 2
    a = array[0] ** 2 + array[1] **2
    if a==b:
        print("right")
    else:
        print("wrong")