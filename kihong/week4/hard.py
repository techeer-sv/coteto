def solution(line):
    from itertools import combinations

    mix_list = set()
    for a_list, b_list in combinations(line, 2):
        a, b, e = map(int, a_list)
        c, d, f = map(int, b_list)
        parent = a * d - b * c
        if parent == 0:
            continue
        else:
            child_x = b * f - d * e
            child_y = e * c - a * f
            if child_x % parent or child_y % parent:
                continue
            else:
                x = child_x // parent
                y = child_y // parent
            mix_list.add((x, y))
    # 교점의 위치를 알았으므로 최소의 높이과 넓이를 구함.
    min_x = min(x for x, _ in mix_list)
    max_x = max(x for x, _ in mix_list)
    min_y = min(y for _, y in mix_list)
    max_y = max(y for _, y in mix_list)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    board = [["."] * width for _ in range(height)]
    for x, y in mix_list:
        board[abs(y - max_y)][abs(x - min_x)] = "*"
    board = ["".join(test) for test in board]
    return board


testcases = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]

board = solution(testcases)
