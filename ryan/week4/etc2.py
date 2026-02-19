from collections import deque
def solution(order):
    answer = 0
    belt1 = deque([0]) # 옮겨 담을수 있는 벨트
    belt2 = deque([0] + [i for i in range(len(order), 0, -1)]) # 원래 벨트
    available = True
    c = 0
    while available and c < len(order):
        i = order[c]
        while True:
            if belt2[-1] == i:
                belt2.pop()
                answer += 1
                break
            elif belt1[-1] == i:
                belt1.pop()
                answer += 1
                break
            elif belt2[-1] != i and belt2[-1] != 0:
                package = belt2.pop()
                belt1.append(package)
            else:
                available = False
                break
        c += 1
    return answer

print(solution([4, 3, 1, 2, 5])) # 2
print(solution([5, 4, 3, 2, 1])) # 5