import sys

N = int(sys.stdin.readline())


def hanoi(n, start, target, sub):
    if n == 1:
        print(start, target)
        return

    hanoi(n-1, start, sub, target)

    print(start, target)

    hanoi(n-1, sub, target, start)


print(2**N - 1)

hanoi(N, 1, 3, 2)