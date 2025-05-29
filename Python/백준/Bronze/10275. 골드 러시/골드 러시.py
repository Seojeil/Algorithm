import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    _, a, b = map(int, input().split())

    print(bin(a).count('1') + bin(b).count('1') - 1)