import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []

def recursion(level,visit):
    visit.sort()
    if level == M:
        if visit not in result:
            result.append(visit)
        return
    for i in range(1, N+1):
        if i not in visit:
            temp = visit.copy()
            temp.append(i)
            recursion(level+1, temp)

recursion(0,[])

for i in result:
    print(' '.join(map(str, i)))