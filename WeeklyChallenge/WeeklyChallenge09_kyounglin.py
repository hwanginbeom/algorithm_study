# 2021-10-14

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/86971

# 9주차_전력망을 둘로 나누기

# dfs계산방식을 잘 몰라 사이트에서 참고함

# 참고 사이트 : https://velog.io/@edhz8888/TIL211006%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%ED%81%B4%EB%A6%AC%EC%B1%8C%EB%A6%B0%EC%A7%80-9%EC%A3%BC%EC%B0%A8

n=9
wires=[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]


from collections import defaultdict

def solution(n, wires):
    graph=defaultdict(list)
    res = 101
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        nodes,cnt,visited=[a],0,[b]
        while nodes:
            node = nodes.pop()
            if node in visited:
                continue
            visited.append(node)
            cnt+=1
            nodes+=graph[node]
        res = min(res,abs(n-cnt*2))
    return res

print(solution(n,wires))