def solution(s):
    answer = ""
    nword = True

    for c in s:
        if c == " ":
            answer += c
            nword = True
        else:
            if nword:
                answer += c.upper()
                nword = False
            else:
                answer += c.lower()

    return answer