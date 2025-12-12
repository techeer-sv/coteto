def solution(clothes):
    dic = {}
    
    answer = 1
    
    for _, k in clothes:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
        
    for v in dic.values():
        answer *= (v+1)
    
    return answer-1
