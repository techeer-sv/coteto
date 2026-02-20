def solution(array):
    array = map(str, array)
    array = "".join(array)
    array = list(array)
    return array.count('7')

print(solution([7, 77, 17]))