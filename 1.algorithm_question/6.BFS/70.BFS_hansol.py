# 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

# 입력값 받기
N, K = map(int, input().split())
# 방문여부 초기값 설정
visited = [False] * 100001

# bfs 함수 정의
def bfs(info):
    # 초기값 설정
    count = 0
    # 시작점 N을 입력받아 [위치, 거리] 형식의 정보가 담긴 리스트로 변형
    q = deque([[info, count]])  # 시작점 설정
    # popleft 와 append 를 반복하는 작업이므로 while 사용
    while q:
        # q에서 [위치, 거리] 정보를 꺼내기
        info = q.popleft()
        # 위치와 거리를 구분해서 변수에 담기
        position = info[0]
        count = info[1]
        # 방문하지 않은 위치라면 방문처리
        # (해당 position 에 가장 먼저 방문했을 때가 최소 count 일 때이므로, 방문했다면 넘어감)
        if not visited[position]:
            visited[position] = True
            # 위치 정보가 찾는 값이라면 count 를 반환
            if position == K:
                return count
            # 아니라면 count 를 1 더하고 해당 위치에서 갈 수 있는 모든 위치를 append
            count += 1
            if (position * 2) <= 100000:
                q.append([position * 2, count])
            if (position + 1) <= 100000:
                q.append([position + 1, count])
            if (position - 1) >= 0:
                q.append([position - 1, count])
    return count

print(bfs(N))
