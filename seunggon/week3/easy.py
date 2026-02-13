def solution(rsp):
    answer = ''
    
    rule = {'2':'0','0':'5','5':'2'}
    
    for i in rsp:
        answer = answer+rule[i]
    
    return answer