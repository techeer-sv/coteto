def solution(answers):
    first = [1,2,3,4,5] #5
    second = [2,1,2,3,2,4,2,5] #8
    third = [3,3,1,1,2,2,4,4,5,5] #10
        
    first_score = 0
    second_score = 0
    third_score = 0
    
    for i in range(len(answers)):
        q = answers[i]
        f_i = i % 5
        s_i = i % 8
        t_i = i % 10
        
        if q == first[f_i]:
            first_score += 1
        if q == second[s_i]:
            second_score += 1
        if q == third[t_i]:
            third_score += 1
    ans = []
    
    vals = [first_score, second_score, third_score]
    max_val = max(vals)
    if first_score == max_val:
        ans.append(1)
    if second_score == max_val:
        ans.append(2)
    if third_score == max_val:
        ans.append(3)
    
    return ans