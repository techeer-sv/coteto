def solution(cards1, cards2, goal):
    cards1.append("")
    cards2.append("")
    p_1 = 0
    p_2 = 0
    for i in goal:
        if i == cards1[p_1]:
            p_1 += 1
        elif i == cards2[p_2]:
            p_2 += 1
        else:
            return "No"
    return "Yes"