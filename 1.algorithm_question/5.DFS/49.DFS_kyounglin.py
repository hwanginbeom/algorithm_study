# 2021-01-11

# 출처 : https://www.acmicpc.net/problem/2583

# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
# 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

# 예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

# <그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지,
#  그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

m,n,k = map(int,input().split())

array=[[0]*n for i in range(m)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

cnt=[]
for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1,y2):
        for q in range(x1,x2):
            array[j][q]=1

for i in range(m):
    for j in range(n):
        if array[i][j]==0:
            count=1
            array[i][j]=1
            queue=[[i,j]]
            while queue:
                x,y=queue[0][0],queue[0][1]
                del queue[0]
                for k in range(4):
                    x1=x+dx[k]
                    y1=y+dy[k]
                    if 0<=x1<m and 0<=y1<n and array[x1][y1]==0:
                        array[x1][y1]=1
                        count+=1
                        queue.append([x1,y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i,end=' ')



# 코드 참고 사이트 : https://pacific-ocean.tistory.com/263
