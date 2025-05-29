import sys

input = sys.stdin.readline

while True:
    M, A, B = map(int, input().split())

    if M == 0 and A == 0 and B == 0:
        break

    time = M * (1/A - 1/B)*60

    hours = int(time//60)
    remaining_minutes = time - (hours * 60)
    minutes = int(remaining_minutes)
    remaining_seconds = (remaining_minutes - minutes) * 60
    seconds = round(remaining_seconds)

    hours = str(hours)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    print(hours + ':' + minutes + ':' + seconds)