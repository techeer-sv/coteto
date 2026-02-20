# 삼각 달팽이 (lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []

    # 행렬 선언
    matrix = [[0]*n for _ in range(n)]
    # 아직 방문하지 않음 = 0

    # 한 변을 갈 때마다 갈 수 있는 칸이 하나씩 줄어듦
    # 처음엔 n칸, 그다음 step에 n-1칸, ...

    flag = 0
    row = -1 # 행
    column = 0 # 열

    num = 0

    while (n>0):
        # flag = 0,1,2 
        # 0 : 아래 (행은 늘어남)
        # 1 : 오른쪽
        # 2 : 대각선 위/왼쪽 (행 -1, 열 -1)
        if flag == 0:
            for _ in range(n):
                row +=1
                # 행이 어디까지 갔었는지 기록을 해놔야함
                num +=1
                matrix[row][column] = num

            flag = 1

        elif flag == 1:
            for _ in range(n):
                column+=1 # column은 한칸 오른쪽으로 가줘야함
                num +=1
                matrix[row][column] = num
                
            flag = 2

        else:
            for _ in range(n):
                row-=1
                column-=1

                num+=1
                matrix[row][column] = num
            
            flag = 0

        n -= 1

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                answer.append(matrix[i][j])

    return answer
