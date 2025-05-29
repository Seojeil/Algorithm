import sys

input = sys.stdin.readline

Q = int(input())

numbers = []

for _ in range(Q):
    numbers.append(int(input()))

for n in numbers:
    if (n & -n) == n:
        print(1)
    else:
        print(0)