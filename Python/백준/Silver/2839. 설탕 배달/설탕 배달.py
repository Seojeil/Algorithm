import sys

input = sys.stdin.readline

weight = int(input())

def sugar(weight):
    if weight == 4 or weight == 7:
        return -1
    
    if weight == 3:
        return 1
    
    if weight % 5 == 0:
        return weight // 5

    dp = {i: [] for i in range(weight // 5 + 2)}

    dp[1] = [3, 5]
    

    for i in range(2, weight//5 + 2):
        for j in dp[i-1]:
            if j+3 == weight:
                return i
            dp[i].append(j+3)
        dp[i].append(max(dp[i-1])+5)
    
    return len(dp)

print(sugar(weight))