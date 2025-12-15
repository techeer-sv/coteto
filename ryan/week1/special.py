def solution(survey, choices):
    answer = ''
    points = {"R" : 0.5, "C" : 0.5, "J" : 0.5, "A" : 0.5,
              "T" : 0, "F" : 0, "M" : 0, "N" : 0}
    priority = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    for i, val in enumerate(survey):
        val_first = val[0]
        val_second = val[1]
        choice = choices[i]
        if choice < 4:
            points[val_first] += (4 - choice)
        else:
            points[val_second] += (choice - 4)
    for x , y in priority:
        if points[x] > points[y]:
            answer += x
        else:
            answer += y
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3]))  # "RCJA"