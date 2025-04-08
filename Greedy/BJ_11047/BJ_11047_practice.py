import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0

coins.reverse()

for coin in coins:
    cnt += K // coin
    K = K % coin

print(cnt)