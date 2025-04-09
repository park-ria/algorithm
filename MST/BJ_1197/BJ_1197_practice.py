import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
result = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    edge[A].append([C, B])
    edge[B].append([C, A])

heap = [[0, 1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        result += w
        for next_heap in edge[each_node]:
            if chk[next_heap[1]] == False:
                heapq.heappush(heap, next_heap)

print(result)