# 기타 그래프 이론 : Kruskal's algorithm

## 신장 트리 

- __그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프__를 의미합니다 
  - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함 

## 최소 신장 트리 

- __최소한의 비용으로 구성되는 신장 트리를 찾아야 할때 어떻게 해야 할까요?__
- 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 가이에 도로를 놓아 __전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우 
  - 두 도시 A,B를 선택했을 떄 A에서 B로 이동하는 경로가 반드시 존재하도록 도로 설치 
- ![image-20201125144537145](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125144537145.png)

## 크루스칼 알고리즘 

- 대표적인 최소 신장 트리 알고리즘 
- 그리디 알고리즘으로 분류 
- 구체적 동작 과정 
  - 1. 간선 데이터를 비용에 따라 __오름차순으로 정렬__
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인 
       1. ) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함 
       2. ) 사이클이 발생하는 경우 최소 신장 트리에 포함 X 
    3. 모든 간선에 대해 2번의 과정을 반복 

- [초기 단계] 그래프의 모든 간선 정보에 대해 __오름차순 정렬 수행__

![image-20201125150151546](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150151546.png)

- [Step 1] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (3,4)를 선택하여 처리 

![image-20201125150233823](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150233823.png)

[Step 2] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (4, 7)을 선택하여 처리

![image-20201125150327347](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150327347.png)

[Step 3] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (4, 6)을 선택하여 처리

![image-20201125150352908](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150352908.png)

[Step 4] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (6, 7)을 선택하여 처리

![image-20201125150418106](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150418106.png)

[Step 5] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (1, 2)을 선택하여 처리

![image-20201125150443302](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150443302.png)

[Step 6] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (2, 6)을 선택하여 처리

![image-20201125150514266](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150514266.png)

[Step 7] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (2, 3)을 선택하여 처리

![image-20201125150539104](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150539104.png)

[Step 8] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (5, 6)을 선택하여 처리

![image-20201125150600516](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150600516.png)

[Step 9] 아직 처리하지 않은 가선 중에서 가장 짧은 간선인 (1, 5)을 선택하여 처리

![image-20201125150626257](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150626257.png)

[알고리즘 수행결과]

- 최소 신장 트리에 포함되어 있는 간선의 비용만 모두 더하면, 그 값이 최종 비용에 해당 

![image-20201125150707158](C:\Users\scoji\AppData\Roaming\Typora\typora-user-images\image-20201125150707158.png)



```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 갯수와 간선 (Union 연산)의 갯수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)   # 부모 테이블 초기화

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a,b, cost = map(int, input().split())
    edges.append((cost, a,b ))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a)  != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost

print(result)
```



## 크루스칼 알고리즘 성능 분석 

- 크루스칼 알고리즘은 간선의 개수가 E개일때, __O(ElogE)__의 시간 복잡도 
- 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선 정렬을 수행하는 부분 
  - 표준 라이브러리를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE) 입니다. 