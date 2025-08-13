import sys

input = sys.stdin.readline

N, game = input().split()

if game == 'Y':
    players = 1
elif game == 'F':
    players = 2
elif game == 'O':
    players = 3

play = []
played = set()
result = 0

for _ in range(int(N)):
    player = input().rstrip()

    if player not in played:
        play.append(player)
        played.add(player)

    if len(play) == players:
        play = []
        result += 1

print(result)