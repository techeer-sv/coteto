def solution(lottos, win_nums):
    c = 0
    for i in win_nums:
        if i in lottos:
            c+=1
    a=[c+lottos.count(0),c]
    s = []
    for c in a:
        if c==6:
            s.append(1)
        elif c==5:
            s.append(2)
        elif c==4:
            s.append(3)
        elif c==3:
            s.append(4)
        elif c==2:
            s.append(5)
        else:
            s.append(6)
    return s




