import sys

input = sys.stdin.readline

angles = set()

while True:
    line = input()

    if line.strip() == '':
        break

    A = int(line.strip())

    if 0 <= A <= 180 and A % 6 == 0:
        print('Y')
    else:
        print('N')