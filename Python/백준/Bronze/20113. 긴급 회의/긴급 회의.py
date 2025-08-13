import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

crew = list(map(int, input().split()))

crew = [v for v in crew if v != 0]

pairs = Counter(crew).most_common()

top_freq = pairs[0][1]
top_vals = [v for v, c in pairs if c == top_freq]

if len(top_vals) > 1:
    print('skipped')
else:
    print(top_vals[0])