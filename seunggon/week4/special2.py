def solution(arr1, arr2):
    m = len(arr1)      
    p = len(arr1[0])  
    n = len(arr2[0])   

    answer = [[0] * n for _ in range(m)]

    for i in range(m):       
        for j in range(n):    
            total = 0        
            for k in range(p): # arr1의 열과 arr2의 행
                total += arr1[i][k] * arr2[k][j]
            
            answer[i][j] = total

    return answer