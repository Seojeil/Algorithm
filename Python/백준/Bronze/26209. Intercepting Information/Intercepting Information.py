import sys

if sum(map(int, sys.stdin.readline().split())) >= 9:
    print('F')
else:
    print('S')
