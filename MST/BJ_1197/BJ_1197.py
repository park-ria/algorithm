"""
1. 개념
  - MST : Minimum Spanning Tree
  - Spanning Tree : 모든 노드가 연결된 트리
  - MST : 최소의 비용으로 모든 노드가 연결된 트리
2. MST 푸는 방법
  - Kruskal : 전체 간선 중 작은 것부터 연결(Union-Find)
  - Prim : 현재 연결된 트리에 이어진 간선 중 가장 작은 것을 추가(heap 자료구조)
3. heap
  - 최대값, 최소값을 빠르게 계산하기 위한 자료구조
  - 이진 트리 구조
  - 처음에 저장할 때부터 최대값, 최소값 결정하도록
4. 아이디어
  - MST 기본문제, 외우기
  - 간선을 인접리스트에 집어넣기
  - 힙에 시작점 넣기
  - 힙이 빌 때까지 다음의 작업을 반복 - 힙의 최소값 꺼내서 해당 노드 방문 안 했다면 방문 표시, 해당 비용 추가, 연결된 간선들 힙에 넣기
5. 시간 복잡도
  - MST : O(ElgE)
6. 자료구조
  - 간선 저장 되는 인접리스트 : (무게, 노드번호)
  - 힙 : (무게, 노드번호)
  - 방문 여부 : bool[]
  - MST 결과값 : int
"""

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

heap = [[0, 1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)