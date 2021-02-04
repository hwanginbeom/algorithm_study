# 스택 자료구조
# 좋은 단어
# https://www.acmicpc.net/problem/3986

N = int(input())
cnt = 0
for _ in range(N):
    check = input()
    stack = []
    # 입력값의 문자를 앞에서부터 체크
    for i in check:
        # stack 이 빈 리스트가 아니고 비교할 문자와
        # stack 의 끝 문자가 같으면 두 문자가 이어지므로 제거
        if stack and stack[-1] == i:
            stack.pop()
        # 빈 리스트거나 끝 문자와 비교할 문자가 다르면
        # 이어질 수 없으므로 append
        else:
            stack.append(i)
    # 모두 이어져서 제거되면 빈 리스트가 되고 이 경우 좋은 단어
    if not stack:
        cnt += 1

print(cnt)