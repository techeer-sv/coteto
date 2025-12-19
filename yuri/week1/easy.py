def solution(nums):
    kind = {}
    
    for i in set(nums):
        kind[i] = 1
        
    if len(kind) > (len(nums) / 2):
        return len(nums) / 2
    
    return len(kind)
