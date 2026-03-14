def solution(n, computers):
    visited = [False] * n
    networks = 0

    def dfs(computer):
        visited[computer] = True

        for next_computer in range(n):
            if computers[computer][next_computer] == 1 and visited[next_computer] == False:
                dfs(next_computer)
            
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            networks += 1

    return networks

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2