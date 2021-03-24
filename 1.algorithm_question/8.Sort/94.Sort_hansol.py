# 정렬
# 접미사 배열
# https://www.acmicpc.net/problem/11656

# 문자 입력
S = input()

# 접미사 배열 입력
lst = []
for i in range(len(S)):
    lst.append(S[i:])

# 정렬 후 출력
lst.sort()
print('\n'.join(lst))
