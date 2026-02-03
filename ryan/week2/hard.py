from collections import defaultdict
from itertools import groupby

def solution(s):
    n = len(s)
    total = n * (n - 1) * (n + 1) // 6
    ext = 0
    unpretty = defaultdict(lambda: defaultdict(int))
    for c, g in groupby(s):
        length = len(list(g))
        unpretty[c][length] += 1
    for i in unpretty:
        print(i, unpretty[i])
    for unpretty_item in unpretty.values():
        t = sum(u * c for u, c in unpretty_item.items())
        print("t:", t)
        both_sides = sum(unpretty_item.values())
        print("both_sides:", both_sides)
        for i in range(1, both_sides + 1):
            ext += t * (t - 1) //2
            t -= both_sides
            both_sides -= unpretty_item[i]
    return total - ext

print(solution("abbcacab"))
