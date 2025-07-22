import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start <= end:
    temp = 0
    mid = (start + end) // 2

    for h in tree:
        if h > mid:
            temp += h - mid

    if temp < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)