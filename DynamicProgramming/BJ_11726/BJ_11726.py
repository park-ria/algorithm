"""
Dynamic Programming이란? 이전의 값을 재활용 하는 알고리즘, 이전의 값을 활용해서 시간복잡도를 줄일 수 있음
1. 아이디어
  - 점화식 : An = An-1 + An-2
  - N 값을 구하기 위해, for문으로 3부터 N까지의 값을 구해주기
  - 이전값, 이전이전값 더해서 10007로 나눠 저장
2. 시간복잡도
  - O(N)
3. 자료구조
  - DP값 저장하는 (경우의 수) 배열 : int[]
  - 최대값 : 10007보다 작음 > int가능
"""

import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2] # 초기값 사각형 0일 때는 0개, 1개일 때는 1개만 나오고 2개일 때는 2개만 나오므로 미리 넣어놓음.

for i in range(3, n+1):
    rs.append((rs[i-1] + rs[i-2]) % 10007)

print(rs[n])