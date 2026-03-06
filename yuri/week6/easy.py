def solution(num):
    answer = 0
    
    if num == 1:
        return answer
    
    for i in range(500):
        if num == 1:
            answer = i
            break
        
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
            
    if answer == 0:
        return -1
        
    return answer
