import sys
input = sys.stdin.readline

hour, minute = map(int, input().split())

if minute < 45:
    minute = minute + 60 - 45
    hour -= 1
else:
    minute = minute - 45

print((hour + 24) if hour < 0 else hour, minute)