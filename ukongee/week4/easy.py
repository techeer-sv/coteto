def solution(array):
    count=0
    for num in array:
        for ch in str(num):
            if ch == '7':
                count+=1
    return count