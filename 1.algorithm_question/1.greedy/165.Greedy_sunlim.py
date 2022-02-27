#백준1026 보물


n= int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


s=0

for i in range(n):
    s+=min(a)*max(b)  #a최소값과 b최대값을 곱해서 s에 더해준다
    a.pop(a.index(min(a))) #a의 최소값 배열에서 빼줌
    b.pop(b.index(max(b)))  #b의 최소값 배열에서 빼줌


print(s)