# 등굣길 (lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    for row in range(len(puddles)):
        puddles[row] = [puddles[row][1],puddles[row][0]]
        puddles[row][0] = puddles[row][0]-1
        puddles[row][1] = puddles[row][1]-1

    map = [[0]*m for _ in range(n)]


    for i in range(0,n):
        for j in range(0,m):
            if i == 0 and j == 0:
                map[i][j] = 1
                continue
            
            if [i,j] in puddles:
                map[i][j] = 0
                continue
                
            up = map[i-1][j] if i>0 else 0
            left = map[i][j-1] if j>0 else 0
            
            map[i][j] = (up+left) % 1000000007

    return map[-1][-1]