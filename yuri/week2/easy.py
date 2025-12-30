def solution(babbling):
    answer = 0
    
    for i in babbling:
        
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
            continue
        
        i = i.replace("aya", " ")
        i = i.replace("ye", " ")
        i = i.replace("woo", " ")
        i = i.replace("ma", " ")
        
        if i.strip() == "":
            answer += 1
    
    return answer
