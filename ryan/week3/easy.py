def solution(rsp):
    d = {"2" : "0", "0" : "5", "5": "2"}
    answer = ""
    for i in rsp:
        answer += d[i]
    return answer