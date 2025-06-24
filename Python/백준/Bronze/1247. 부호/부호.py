import sys

input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    test = 0

    for _ in range(N):
        test += int(input())

    if test > 0:
        print('+')
    elif test < 0:
        print('-')
    else:
        print(0)
