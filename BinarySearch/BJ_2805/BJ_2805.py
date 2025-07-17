import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for height in tree:
        if height > mid:
            sum += height - mid

    if sum < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)