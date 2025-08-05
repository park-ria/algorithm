import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
print(visited)

dy = [0,1,0,-1]
dx = [1,0,-1,0]