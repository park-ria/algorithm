import sys
input = sys.stdin.readline

N = int(input())
cardList = sorted(list(map(int, input().split())))
M = int(input())
targetList = list(map(int, input().split()))

count = {}
for card in cardList:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

print(*[count.get(t, 0) for t in targetList])