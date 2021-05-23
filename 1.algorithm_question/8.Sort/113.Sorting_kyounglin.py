# 2021-05-23


import sys
input=sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

check=list(sorted(set(array)))

# a.index(i) -> 인덱스 함수 사용하면 시간초과ㅠㅠ 이기 때문에 딕셔너리로 인덱스를 저장하는게 좋음
dict = {check[i] : i for i in range(len(check))}

for i in array:
    print(dict[i],end=' ')