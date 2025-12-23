def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        val = arr[i]
        arr[i] = val.lower().capitalize()
    return ' '.join(arr)