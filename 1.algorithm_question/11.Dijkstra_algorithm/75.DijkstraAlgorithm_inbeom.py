'''
문제
예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다. 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고
낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다. 서강그라운드에서 1등을 하면 보상으로 치킨을
주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다. 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이
없어서라고 생각한 예은이는 낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만
어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.
각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다. 예은이는 낙하한
지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수
있는 아이템의 최대 개수를 알려주자.
주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. ( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선
위의 숫자는 거리를 의미한다) 예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다.
(4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.) 이렇게 되면 예은이는
23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.

입력
첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.
둘째 줄에는 n개의 숫자가 차례대로  각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.
세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.

출력
예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.
'''

# 다익스트라의 빠른 실행을 위해 heapq 모듈 import
import heapq, sys

# 최대값 할당
INF = 99999999999999999999999

# 입력부
vertex, limit, edge = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

# 인접 리스트 생성
adj = [[] for _ in range(vertex)]
for i in range(edge):
    x, y, z = map(int, sys.stdin.readline().split())
    adj[x - 1].append((y - 1, z))
    adj[y - 1].append((x - 1, z))


# dijkstra : 다익스트라 알고리즘 함수
def dijstra(v):
    d[v] = 0
    min_q = []
    min_q.append((d[v], v))
    while len(min_q) != 0:
        distance = min_q[0][0]
        current = min_q[0][1]
        heapq.heappop(min_q)
        if d[current] < distance:
            continue
        for i in range(len(adj[current])):
            next = adj[current][i][0]
            nextdistance = adj[current][i][1] + distance
            if nextdistance < d[next]:
                d[next] = nextdistance
                heapq.heappush(min_q, (nextdistance, next))


# 각 정점에 대해 다익스트라 실행
ans = 0
for i in range(vertex):
    d = [INF] * vertex
    dijstra(i)
    cnt = item[i]
    for j in range(vertex):
        # 만일 j가 i가 아니고 수색범위 이내라면
        # cnt에 정점 j에서 얻을 수 있는 아이템 수를 더해줌
        if d[j] != 0 and d[j] <= limit:
            cnt += item[j]
    # 최대값 갱신
    if ans < cnt:
        ans = cnt
print(ans)



#
#
# import heapq  # 우선순위 큐 구현을 위함
#
#
# def dijkstra(graph, start, ranges, area):
#     # distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
#     # INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
#     distances = [0] * (area + 1)
#     # print(distances)
#     distances[start] = 0  # 시작 값은 0이어야 함
#     queue = []
#     heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.
#     # print(queue, [distances[start], start])
#     # print(graph)
#     while queue:  # queue에 남아 있는 노드가 없으면 끝
#         # print(queue)
#         current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
#         # print(current_distance)
#         # print(current_destination )
#         # print(current_distance)
#         if ranges < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#             continue
#         # print(graph[current_destination])
#         for i in graph[current_destination]:
#             new_destination = i[0]
#             new_distance = i[1]
#
#             distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
#             if distance <= ranges:  # 알고 있는 거리 보다 작으면 갱신
#                 distances[new_destination] = distance
#                 heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
#             # else:
#             #     distances
#
#     return distances
#
#
# area, ranges, way = map(int, input().split())
# # area, ranges, way = 5, 5, 4
#
# # print(area, ranges, way)
# items = [int(x) for x in input().split()]
# # items = [5, 7, 8, 2, 3]
# #
# graph = [[]for i in range(area + 1)]
#
# for _ in range(way):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))
# # graph = [[], [(4, 5), (2, 3)], [(5, 4), (3, 3), (1, 3)], [(2, 3)], [(1, 5)], [(2, 4)]]
# # print(graph)
# # print(graph)
#
#
# graph2 = []
# sum_items  = []
# for start in range(1, area+1):
#     # print(start)
#     graph2 = dijkstra(graph, start, ranges, area)
#     sum_item = items[start-1]
#     for i in range(area+1):
#         if graph2[i] != 0:
#             sum_item += items[i-1]
#     else:
#         sum_items.append(sum_item)
# print(sum_items)
# print(max(sum_items))