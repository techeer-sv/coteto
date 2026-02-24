def solution(x):
    # f = [0, 1, 1, 2, 3, 5]
    f = [0] * (x+1)
    f[0] = 0
    f[1] = 1
    
    for i in range(2, x+1):
        f[i] = f[i-2] + f[i-1]
    
    return f[-1] % 1234567
