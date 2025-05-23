import sys

C = sys.stdin.readline().strip()

grade = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}
additional = {'+': 0.3, '0': 0, '-': -0.3}

if C == 'F':
    print(0.0)
else:
    print(grade[C[0]] + additional[C[1]])