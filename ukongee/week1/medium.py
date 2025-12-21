def solution(clothes):
    cloth_count = {}

    for item in clothes:
        kind = item[1]
        cloth_count[kind] = cloth_count.get(kind, 0) + 1

    result = 1
    for count in cloth_count.values():
        result *= (count + 1)

    return result - 1
