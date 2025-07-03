import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()

def search(start, end, target):
    if start == end:
        if nums[start] == target:
            print(1)
        else:
            print(0)
        return

    middle = (start + end) // 2
    if nums[middle] < target:
        search(middle + 1, end, target)
    else:
        search(start, middle, target)

for target_each in target_list:
    search(0, N-1, target_each)