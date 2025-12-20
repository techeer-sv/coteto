def solution(clothes):
    
    clothes_len = len(clothes) # 의상 개수
    kind_arr = [] # 의상 종류
                
    for i in clothes:
        if i[1] not in kind_arr:
            kind_arr.append(i[1])
    
    dic = {}
    for i in kind_arr:
        dic[i] = 1
    
    for i in range(clothes_len):
        dic[clothes[i][1]] += 1
        
    kind_num = list(dic.values())
    
    tmp = 1
    for i in range(len(kind_num)):
        tmp *= kind_num[i]
        
    return tmp - 1
    
