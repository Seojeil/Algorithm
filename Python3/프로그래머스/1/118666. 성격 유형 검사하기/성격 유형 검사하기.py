def solution(survey, choices):
    index = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    
    for s in range(len(survey)):
        if choices[s] > 4:
            index[survey[s][1]] += (choices[s]-4)
        elif choices[s] < 4:
            index[survey[s][0]] -= (choices[s]-4)
    
    if index['R'] >= index['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if index['C'] >= index['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if index['J'] >= index['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if index['A'] >= index['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer