"""
그리디란? 현재 차례의 최고의 답을 찾는 문제
1. 아이디어
  - K를 큰 금액의 동전부터 나눈 뒤 남은 값으로 갱신
  - 동전을 저장한 뒤, 내림차순으로 정렬
  - 동전 for문
    - 동전 사용개수 추가
    - 동전 사용한만큼 K값 갱신
2. 시간복잡도
  - O(N)
3. 자료구조
  - 동전 금액: int[] => 최대값: 1e^6 => int 가능
  - 현재 남은 금액: int => 최대값: 1e^8 => int 가능
  - 동전 개수: int => 최대값: 1e^8 => int 가능
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)
