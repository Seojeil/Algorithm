import sys

input = sys.stdin.readline

father_body, father_tail = input().split()
mother_body, mother_tail = input().split()

colors = list(set([father_body, father_tail, mother_body, mother_tail]))

colors.sort()

for body in colors:
    for tail in colors:
        print(body, tail)