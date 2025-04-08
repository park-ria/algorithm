"""
1. 아이디어
  - 이진 탐색은 무조건 정렬이 되어있어야 함
  - N개의 수 먼저 정렬
  - M개를 for 돌면서 이진 캄색으로 확인
  - 이진탐색 안에서 마지막에 데이터 찾으면 1, 아니면 0 출력
2. 시간복잡도
  - M개의 수 : O(M) = 100000 = 1e^5, N개의 수 : O(N) = 100000 = 1e^5 => O(MN) = 1e^10 > 2억 초과 불가
  - 그럼 투포인터 생각 할 수 있으나 투포인터는 연속된 경우에 적용 가능 근데 이건 연속되지 않고 어떤 값이 있는지 찾아내는 문제이기 때문에 이진탐색
  - N개의 수 정렬 : O(N*lgN)
  - M개의 수 이진탐색 : O(M*lgN)
  - 이진탐색의 로그는 log 밑이 2 임 -> log2 10^5 => 계산하기 쉽게 log2 10^6 이라고 하면 log2 10^3 + log2 10^3 = log2 2^10 + log2 2^10 = 10+10 = 20
  - O((N+M)lgN) = (1e^5 + 1e^5) * log10^5 => 2e^5 * 20 = 4e^6 < 2억 => 가능
3. 자료구조
  - 탐색 대상 수(N개 숫자) : int[] = -2^31 ~ 2^31 > int 가능(파이썬은 int 고려안해도 됨)
  - 탐색 하려는 수(M개 숫자) : int[] = -2^31 ~ 2^31 > int 가능(파이썬은 int 고려안해도 됨)
Tip
  - 어떤 값을 여러번 탐색해야 하는 경우 입력의 개수가 1e^5 정도의 경우라면 이진탐색 의심
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

# 이진탐색을 위해 정렬
nums. sort()

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en)//2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

for each_target in target_list:
    search(0, N-1, each_target)