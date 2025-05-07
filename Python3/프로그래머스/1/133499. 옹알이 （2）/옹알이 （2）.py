def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    
    for b in baby:
        babbling = [x for x in babbling if b*2 not in x]

    for b in baby:
        babbling = [word.replace(b, ' ') for word in babbling]
        
    for _ in babbling:
        babbling = [word.replace(' ', '') for word in babbling]

    answer = babbling.count('')

    return answer


