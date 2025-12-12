def solution(nums):
    set_nums = set(nums)
    set_len = len(set_nums)
    nums_len = len(nums)/2
    
    if set_len > nums_len:
        return nums_len
    else:
        return set_len
    