import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

N = len(S)

prefix_sum = {}

for target_char in set(S):
    temp_list = [0] * (N + 1)
    
    count = 0
    
    for i in range(N):
        if S[i] == target_char:
            count += 1

        temp_list[i+1] = count

    prefix_sum[target_char] = temp_list

for _ in range(q):
    a, l, r = input().split()

    l, r = int(l), int(r)

    if a in prefix_sum:
        print(prefix_sum[a][r+1] - prefix_sum[a][l])
    else:
        print(0)