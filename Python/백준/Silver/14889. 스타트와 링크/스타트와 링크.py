from itertools import combinations

t = int(input())
team = []
for _ in range(t):
    team.append(list(map(int, input().split())))

result = float("inf")

# 절반의 조합만 고려 (첫 번째 사람은 항상 team_1에 포함)
for comb in combinations(range(1, t), t//2 - 1):
    team_1 = [0] + list(comb)
    team_2 = [i for i in range(t) if i not in team_1]
    
    start_ab = 0
    link_ab = 0
    
    # 중복 없이 팀 능력치 계산
    for i in range(len(team_1)):
        for j in range(i+1, len(team_1)):
            s1, s2 = team_1[i], team_1[j]
            start_ab += team[s1][s2] + team[s2][s1]
    
    for i in range(len(team_2)):
        for j in range(i+1, len(team_2)):
            l1, l2 = team_2[i], team_2[j]
            link_ab += team[l1][l2] + team[l2][l1]
    
    result = min(result, abs(start_ab - link_ab))
    
    if result == 0:
        break

print(result)