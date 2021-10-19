def solution(n, wires):
    answer = n
    tree = {k: set() for k in range(1, n + 1)}
    for a, b in wires:
        tree[a].add(b)
        tree[b].add(a)
    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        result = abs(2 * dfs(a, tree) - n)
        tree[a].add(b)
        tree[b].add(a)
        answer = min(answer, result)
    return answer

def dfs(start, tree):
    queue = [start]
    marked = {start}
    while queue:
        v = queue.pop()
        for w in tree[v]:
            if w not in marked:
                queue.append(w)
                marked.add(w)
    return len(marked)




n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
solution(n, wires)
