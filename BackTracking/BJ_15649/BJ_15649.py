"""
1. 아이디어
  - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
  - 재귀함수에서 M개를 선택할 경우 프린트
2. 시간 복잡도
  - N^N : 중복 가능, N = 8까지 가능
  - N! : 중복 불가, N = 10까지 가능
  => 이 문제는 중복불가이기 때문에 N!
3. 자료구조
  - 방문 여부 체크 배열 : bool[]
  - 결과값 저장 배열 : int[]
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
check = [False] * (N+1) # 0부터 N-1이 아닌 1부터 N까지 접근하기 위해 처음부터 N+1로 줌
print(check)

def recur(num) :
    if num == M :
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num+1)
            check[i] = False
            result.pop()
recur(0)