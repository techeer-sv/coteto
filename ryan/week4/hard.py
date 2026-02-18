def solution(line):
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')

    answer = set()

    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]

            denom = a*d - b*c
            if denom == 0:
                continue

            x_num = b*f - e*d
            y_num = e*c - a*f

            if x_num % denom == 0 and y_num % denom == 0:
                x = x_num // denom
                y = y_num // denom

                x_min = min(x_min, x)
                x_max = max(x_max, x)
                y_min = min(y_min, y)
                y_max = max(y_max, y)

                answer.add((x, y))

    width = x_max - x_min + 1
    height = y_max - y_min + 1

    canvas = [["."] * width for _ in range(height)]

    for x, y in answer:
        canvas[y - y_min][x - x_min] = "*"

    return ["".join(row) for row in canvas[::-1]]


print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))