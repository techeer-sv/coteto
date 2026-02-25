def solution(triangle):
    '''
        [7]
       [3, 8]
      [8, 1, 0]
     [2, 7, 4, 4]
    [4, 5, 2, 6, 5]
    '''
    
    '''
        [7]
      [10, 15]
    [18, 16, 15]
  [20, 25, 20, 19]
 [24, 30, 27, 26, 24]
    '''
    
    # d[i]: 해당 층까지의 합이 가장 큰 경우
    d = triangle
    d[1][0] += d[0][0]
    d[1][1] += d[0][0]
    
    # print(triangle)
    
    for i in range(2, len(triangle)):
        d[i][0] += d[i-1][0]
        d[i][-1] += d[i-1][-1]
        
        for j in range(1, len(triangle[i])-1):
            d[i][j] += max(d[i-1][j-1], d[i-1][j])
    
    return max(d[-1])
