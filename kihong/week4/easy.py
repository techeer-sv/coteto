def solution(array):
    count = 0
    for i in array:
        num = list(map(int, str(i).strip()))
        count += num.count(7)
    return count


inputs = [[7, 77, 17], [10, 29]]

for input in inputs:
    print(solution(input))  # 4, 0
