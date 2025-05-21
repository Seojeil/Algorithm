import sys

N = int(sys.stdin.readline())


def hanoi(n, start, target, sub, move, path):
    if n == 1:
        path.append((start, target))
        return move + 1, path

    move, path = hanoi(n-1, start, sub, target, move, path)

    path.append((start, target))
    move += 1

    move, path = hanoi(n-1, sub, target, start, move, path)

    return move, path


move = 0
path = []

move, path = hanoi(N, 1, 3, 2, move, path)

print(move)

for s, t in path:
    print(s, t)