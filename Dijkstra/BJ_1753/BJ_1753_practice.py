import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

dist = [INF for _ in range(V+1)]
dist[K] = 0

heap = [[0, K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: #오답 이해 못했었음 : 다익스트라는 최소 거리부터 순차적으로 처리하므로 dist[ev] > ew가 발생하지 않음
        continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw #오답 여기 dist[ev] = ew + nw라고 풀었었음
            heapq.heappush(heap, [dist[nv], nv]) #오답 heapq.heappush(heap, [dist[nw], nw])라고 풀었었음

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])