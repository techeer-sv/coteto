def solution(nums):
    # 고를 수 있는 마리 수
    pick = len(nums) // 2

    # 서로 다른 종류 수
    kinds = len(set(nums))

    # 종류를 최대한 많이 고르려면
    # (서로 다른 종류 수)와 (고를 수 있는 마리 수) 중 작은 값이 정답
    return min(kinds, pick)
