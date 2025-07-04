import sys
input = sys.stdin.readline

N = int(input())
cardList = sorted(list(map(int, input().split())))
M = int(input())
targetList = list(map(int, input().split()))
resultList = [0] * M


def search(start, end, target, index):
    if start > end:
        return

    mid = (start+end) // 2

    if cardList[mid] == target:
        resultList[index] += 1


for index, target in enumerate(targetList):
    search(0, N-1, target, index)

print(*resultList)

# for result in resultList:
#     print(' '.join(map(str, result)))