def solution(array):
    answer = 0
    
    for i in range(len(array)):
        for j in range(len(str(array[i]))):
            if str(array[i])[j] == '7':
                answer += 1
    return answer
