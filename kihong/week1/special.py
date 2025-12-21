def solution(survey, choices):

    scores = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    length = len(survey)

    for idx in range(length):
        num = choices[idx] - 4
        score = abs(num)
        if num < 0:
            scores[survey[idx][0]] += score
        else:
            scores[survey[idx][1]] += score
    result = []
    items = list(scores.items())
    for idx in range(0, 8, 2):
        if items[idx][1] > items[idx + 1][1]:
            result.append(items[idx][0])
        elif items[idx][1] < items[idx + 1][1]:
            result.append(items[idx + 1][0])
        else:
            result.append(sorted(list([items[idx][0], items[idx + 1][0]]))[0])

    return "".join(result)


survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
print(solution(survey, choices))
