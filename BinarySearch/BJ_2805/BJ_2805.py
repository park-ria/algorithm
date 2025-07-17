import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    hSum = 0
    mid = (start + end) // 2

    for height in tree:
        if height > mid:
            hSum += height - mid

    if hSum < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)