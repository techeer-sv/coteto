def solution(clothes):
    d = {}
    for item, category in clothes:
        if category not in d:
            d[category] = 2
        else:
            d[category] += 1
    answer = 1
    for i in d.values():
        answer *= i
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))  # 3