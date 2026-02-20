def solution(line):
    cross = []

    for i in range(len(line)): # 직선 두 개 씩 비교 # 0,1,2,3,4
        for j in range(i+1,len(line)): # 1,2,3,4. i = 3 일 때 j가 4부터 시작하고 이는 len(line)-1 과 같음
            a,b,e = line[i] 
            c,d,f = line[j] 

            if (a*d - b*c) == 0:
                continue

            x = ( b*f - e*d ) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                cross.append([x,y])

    top = max(i[1] for i in cross)
    bottom = min(i[1] for i in cross)
    left = min(i[0] for i in cross)
    right = max(i[0] for i in cross)

    answer = []
    for _ in range(top - bottom + 1):
        row = []
        for _ in range(right - left + 1):
            row.append('.')
        answer.append(row)
        
    # answer = [['.' for _ in range(right - left + 1)] for _ in range(top - bottom + 1)]

    for point in cross:
        # [3,2] 의 y값 2
        # max인 4와 얼마나 차이나는가?
        # 2만큼 작음 = index 0에서 +2

        # x값도 left와 얼마나 차이나는지 비교
        answer[top-point[1]][point[0]-left] = "*" # [세로][가로]

    answer = ["".join(row) for row in answer]
    
    return answer