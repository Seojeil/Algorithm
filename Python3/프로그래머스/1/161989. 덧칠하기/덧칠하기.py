def solution(n, m, section):
    
    answer = 0
    n = 0
    
    for i in section:
        if i >= n:
            print(i)
            answer += 1
            n = i + m
            
    
    return answer