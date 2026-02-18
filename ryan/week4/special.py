def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]

    x = -1
    y = 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            # 위에서 왼쪽에서 아래로
            if i % 3 == 0:
                x += 1
            # 아래에서 오른쪽으로
            elif i % 3 == 1:
                y += 1
            # 오른쪽에서 위로
            elif i % 3 == 2:
                y -= 1
                x -= 1

            snail[x][y] = num
            num += 1
    answer = []
    for i in snail:
        answer += i
    return answer

print(solution(4))