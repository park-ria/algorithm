import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
cnt = 0

while 1:
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1

    sw = False
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                y = ny
                x = nx
                d = (d - i + 4) % 4
                sw = True
                break

    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)