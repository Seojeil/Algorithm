import sys

result = []

T, F, S, P, C = map(int, sys.stdin.readline().split())

result.append(T*6 + F*3 + (S+C)*2 + P*1)

T, F, S, P, C = map(int, sys.stdin.readline().split())

result.append(T*6 + F*3 + (S+C)*2 + P*1)

a, b = result

print(a, b)