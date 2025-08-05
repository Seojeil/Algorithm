import sys

input = sys.stdin.readline


cho = list(map(int, input().split()))
han = list(map(int, input().split()))

cho_score = 0
han_score = 1.5

start = [2, 2, 2, 2, 2, 5]
score = [13, 7, 5, 3, 3, 2]

for i in range(6):
    cho_score += ((cho[i] - start[i]) * score[i])
    han_score += ((han[i] - start[i]) * score[i])

if han_score >= cho_score:
    print("ekwoo")
else:
    print("cocjr0208")