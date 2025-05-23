import sys

N = int(sys.stdin.readline())

result = ((N**2)*3 + N*5 + 2)//2

print(result % 45678)