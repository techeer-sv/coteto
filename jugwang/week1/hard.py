def solution(genres, plays):
    answer = []
    d = {}
    total = {}
    
    for i, g in enumerate(genres):
        if g in d:
            d[g].append(i)
        else:
            d[g] = []
            d[g].append(i)
        if g in total:
            total[g] += plays[i]
        else:
            total[g] = plays[i]    
    
    for k,_ in sorted(total.items(), key = lambda x:x[1], reverse=True):
        for i in sorted(d[k], key=lambda x: plays[x], reverse=True)[:2]:
            answer.append(i)
        
    return answer