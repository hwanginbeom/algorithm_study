n, m = map(int, input().split())

not_listen = []
not_look = []
for _ in range(n) :
    not_listen.append(input())
for _ in range(m) :
    not_look.append(input())

answer = list(set(not_listen) & set(not_look))
answer.sort()

print(len(answer))
for i in answer :
    print(i)