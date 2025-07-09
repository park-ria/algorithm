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

def search(start, end, target):
    if start > end:
        return 0

    mid = (start+end) // 2

    if cardList[mid] == target:
        return count[target]
    elif cardList[mid] < target:
        return search(mid+1, end, target)
    else:
        return search(start, mid-1, target)

for target in targetList:
    print(search(0, N-1, target), end=" ")