def solution(lottos, win_nums):
    zero = 0
    match = 0

    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            match += 1

    best = match + zero
    worst = match

    rank_map = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }

    return [rank_map[best], rank_map[worst]]
