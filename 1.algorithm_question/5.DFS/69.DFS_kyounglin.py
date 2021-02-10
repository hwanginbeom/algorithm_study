# 2021-02-10

# 출처 : https://www.acmicpc.net/problem/1987

# 알파벳

# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# python3 -> 시간 초과 pypy3 -> 매우 느리게 통과...

def dfs(x,y,count): # dfs,bfs는 정말정말 잘 모르겠다...ㅠ
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    stay=(x,y)

    global answer
    answer=max(answer,count)

    for i in range(4):
        nx=stay[0]+dx[i]
        ny=stay[1]+dy[i]

        if (0<=nx<r) and (0<=ny<c):
            if alphabet[array[nx][ny]]==0:
                alphabet[array[nx][ny]] = 1 # 방문처리

                dfs(nx,ny,count+1)
                alphabet[array[nx][ny]] =0 # 백트래킹 : 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아감


r,c=map(int,input().split())
array=[]
for _ in range(r):
    check = []
    for i in list(input()):
        check.append(ord(i)-65) #slicing을 위해 문자를 숫자로 바꿔줄 필요가 있었음 알파벳 리스트를 인덱스 번지로 위치 찾기 위해
    array.append(check)



alphabet=[0]*26
alphabet[array[0][0]]=1
answer=1 # 시작점에서도 카운트 필요
dfs(0,0,answer)

print(answer)


