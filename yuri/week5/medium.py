def solution(land):
    '''
    [1,2,3,5]
    [10,11,12,11]
    [16,15,13,13]
    '''
    
    for row in range(1, len(land)):
        for col in range(len(land[0])):
            land[row][col] += max(land[row-1][:col] + land[row-1][col+1:])
    
    return max(land[-1])
    
