import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

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

dfsResult = []
dfs(v)
print(*dfsResult)