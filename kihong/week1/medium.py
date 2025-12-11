def solution(clothes):
    cloth_dict = dict()

    for name, cloth_type in clothes:
        if cloth_type not in cloth_dict:
            cloth_dict[cloth_type] = [name]
        else:
            cloth_dict[cloth_type].append(name)

    result = 1
    for item_list in cloth_dict.values():
        count = len(item_list)
        result *= count + 1
    return result - 1


sample = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
result = solution(sample)

print(result)
