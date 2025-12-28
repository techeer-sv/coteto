def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        valid = True
       
        for i in pron:
            if i * 2 in word:  # "ayaaya" 확인
                valid = False
                break
        
        if not valid:
            continue
            
        for j in pron:
            word = word.replace(p, " ") # 발음 가능한 부분 -> 공백 
        
        if word.strip() == "":
            answer += 1
            
    return answer