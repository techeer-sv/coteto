def solution(cards1, cards2, goal):
    
    for i in range(len(goal)):
        if len(cards1) != 0:
            if goal[i] == cards1[0]:
                cards1.pop(0)
                continue
        if len(cards2) != 0:
            if goal[i] == cards2[0]:
                cards2.pop(0)
                continue
        return "No"
    
    return "Yes"
