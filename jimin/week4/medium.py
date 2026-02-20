def solution(answers):
    result = []
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(answers)):
        if answers[i] == user1[i%len(user1)]:
            c1+=1
        if answers[i] == user2[i%len(user2)]:
            c2+=1
        if answers[i] == user3[i%len(user3)]:
            c3+=1

    scores = [c1, c2, c3]
    m = max(scores)

    for idx in range(3):
        if scores[idx] == m:
            result.append(idx + 1)


    return result