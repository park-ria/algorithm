"""
1. 작동원리
  - 간선 : 인접 리스트, 거리 배열 : 초기값 무한대로 설정, 힙 시작점 추가
  - 힙에서 현재 노드 빼면서, 간선 통할 때 더 거리 짧아진다면 거리 갱신 및 힙에 추가
2. 아이디어
  - 한 점에서 다른 모든 점으로의 최단경로 > 다익스트라 사용
  - 간선, 인접리스트 저장
  - 거리 배열 무한대 초기화
  - 시작점 : 거리 0, 힙에 추가
  - 힙에서 하나씩 빼면서 수행할 것
    - 최신값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신
3. 시간복잡도
  - 다익스트라 시간복잡도 : O(ElogV)
  - E : 3e5
  - V : 2e4, lgV ~= 20
  - ElgV = 6e6 가능
4. 자료구조
  - 힙 : (비용, 노드번호)
  - 거리 배열 : 비용 int[]
  - 간선 저장, 인접리스트 : (비용, 노드번호)[]
"""

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V+1)]

# 거리배열
dist = [INF] * (V+1)

for i in range(E):
    # u : 시작점, v : 도착점, w : 비용
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

# 시작점 초기화
dist[K] = 0
heap = [[0, K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])