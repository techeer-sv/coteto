def solution(lottos, win_nums):
    zeroes = lottos.count(0)
    common = len(set(lottos) & set(win_nums))
    return [min(7 - (common + zeroes), 6), min(7 - common, 6)]