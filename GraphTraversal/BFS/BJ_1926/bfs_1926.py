import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
print(visited)

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = [(y,x)]
    while q :
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0 <= nx < m:
                if map[ny][nx] == 1 and visited[ny][nx] == False:
                    rs += 1
                    visited[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
