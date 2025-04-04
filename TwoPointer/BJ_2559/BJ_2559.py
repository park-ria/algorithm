"""
  N : 온도를 측정한 전체 날짜의 수
  K : 연속적인 날짜의 수
  1. 아이디어
    - 투포인터를 활용
    - for문으로 처음에 k개 값을 저장
    - 다음 인덱스 더해주고 이전 인덱스 빼줌
    - 이때마다 최대값 갱신
  2. 시간 복잡도
    - O(N) = 1e5 > 가능
  3. 자료구조
    - 각 숫자들 N개 저장 배열 : int[]
    - 숫자 최대 100 > int 가능
    - K개의 값을 저장하는 변수 : int
    - 최대 : K * 100 = 1e5 * 100 = 1e7 > int가능
    - 최대값 : int

Tip
  1. 처음부터 생각하기 어려우므 쉬운방법부터 생각
    - O(N^2) 시간 복잡도가 2억을 초과한다면
    - 연속하다는 특징을 활용할 수 있는지 확인
  2. for 내부 투포인터 계산하는 값의 최대값 확인 필수(INT초과) -> 파이썬은 해당 안됨
  3. 투포인터 문제 종류
    - 두개 다 왼쪽에서 / 각각 왼쪽, 오른쪽 / 다른배열
    - 일반 O(N) / 정렬 후 투포인터: O(NlgN)
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0

# K개를 더해주기
for i in range(K):
    each += nums[i]
maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)