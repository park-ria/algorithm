import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(index):
    visited[index] = True
    dfsResult.append(index)

    graph[index].sort()
    for i in graph[index]:
        if not visited[i]:
            dfs(i)

visited = [False] * (n+1)
dfsResult = []
dfs(v)
print(*dfsResult)

def bfs(index):
    q = []
    q.append(index)

    visited[index] = True
    bfsResult.append(index)

    while q:
        current = q.pop(0)
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                bfsResult.append(i)
                q.append(i)

visited = [False] * (n+1)
bfsResult = []
bfs(v)
print(*bfsResult)