def solution(nums):
    max_pick = len(nums)/2
    unique_count = len(set(nums))
    return min(max_pick, unique_count)