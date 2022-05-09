# -*- coding: utf-8 -*-

#소수사이 수열
#백준3896

T = int(input())
arr = [int(input()) for _ in range(T)]
max_num = max(arr)
arr_check = [0 for _ in range(1299710)]     # 소수 판정 소수면 0
                                           # 0, 1도 소수가 아니지만 안쓰니까 그냥 둔다.






for i in range(2, 1299710):                 # 에라토스테네스의 체 배열 구현
    if arr_check[i] == 0:                   # 소수 발견
        if max_num <= i:                     # max_num 보다 크거나 같은 소수를 만나면 종료
            break
        for j in range(i*i, 1299710, i):    # 소수가 아닌 수에 1로 변경
            arr_check[j] = 1                # i보다 작은 수로 곱하는 경우는 이미 나왔다.





for i in arr:
    if arr_check[i]:    # 합성수일경우 왼쪽 오른쪽 소수를 찾는다.
        dl = i - 1      # 왼쪽 탐색
        dr = i + 1      # 오른쪽 탐색
        while arr_check[dl] or arr_check[dr]:   # 왼쪽과 오른쪽 다 소수를 만났을 때 탈출
            if arr_check[dl]:       # 소수가 아니면 왼쪽으로 1칸 이동
                dl -= 1
            if arr_check[dr]:       # 소수가 아니면 오른쪽으로 1칸 이동
                dr += 1
        print(dr - dl)              # 두 소수의 길이 출력
    else:                           # 소수일 경우 0 print
        print(0)