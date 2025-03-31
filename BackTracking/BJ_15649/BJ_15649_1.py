import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def recursion(level, visit) :
    if level == M:
        print(' '.join(map(str, visit)))
        return
    for i in range(1, N+1):
        if i not in visit:
            temp = visit.copy()
            temp.append(i)
            recursion(level+1, temp)

recursion(0, [])