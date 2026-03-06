def solution(num):
    for count in range(500):
        if num == 1:
            return count

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

    return -1