import sys

input = sys.stdin.readline

X, Y = map(int, input().split())


def repunit(n):
    return int('1'*n)


print(repunit(X) + repunit(Y))