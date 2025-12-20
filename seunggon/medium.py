def solution(clothes):
    # 각 타입에 해당하는 의상에 + 1 하고 다 곱하면 되는듯

    type_counts = dict()

    for name,type in clothes:
        if type in type_counts:
            type_counts[type] += 1 # 이 딕셔너리에선 type이 키가 됨
        else: # 없었다면 딕셔너리에 key를 추가하고 1을 넣어둔다
            type_counts[type] = 1

    # 예) 
    # [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] 이면
    # type_counts  = {"headgear": 2, "eyewear": 1}
        
    answer = 1
    for i in type_counts.values():
        answer *= (i + 1)

    answer -=1

    return answer