import sys

input = sys.stdin.readline

mix = input()

cups = [1, 0, 0]

for m in mix:
    if m == "A" and cups[2] != 1:
        cups[0], cups[1] = cups[1], cups[0]
    elif m == "B" and cups[0] != 1:
        cups[1], cups[2] = cups[2], cups[1]
    elif m == "C" and cups[1] != 1:
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1)+1)