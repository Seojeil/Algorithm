import sys

input = sys.stdin.readline

_ = int(input())
line = list(map(int, input().split()))

result = 0

for n, m in enumerate(line):
    if m - (n+1) != 0:
        result += 1

print(result)