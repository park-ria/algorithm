"""
N : 정점의 개수
M : 간선의 개수
V : 시작 정점 번호
"""

import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M) :
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) #양방향

# 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

def dfs(num):
    visit[num] = True
    ans_dfs.append(num)
    for i in graph[num]:
        if not visit[i] :
            dfs(i)

def bfs(num):
    q = []
    q.append(num)
    ans_bfs.append(num)
    visit[num] = True

    while q:
        current = q.pop(0)
        for i in graph[current]:
            if not visit[i]:
                visit[i] = True
                q.append(i)
                ans_bfs.append(i)


visit = [False]*(N+1)
ans_dfs = []
dfs(V)

visit = [False]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)