def solution(land):
    prev_max = land[0]

    for i in range(1, len(land)):
        current = [0, 0, 0, 0]
        
        current[0] = land[i][0] + max(prev_max[1], prev_max[2], prev_max[3])
        current[1] = land[i][1] + max(prev_max[0], prev_max[2], prev_max[3])
        current[2] = land[i][2] + max(prev_max[0], prev_max[1], prev_max[3])
        current[3] = land[i][3] + max(prev_max[0], prev_max[1], prev_max[2])
        
        prev_max = current

    return max(prev_max)