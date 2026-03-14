def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    route = ["ICN"]
    
    def dfs(current):
        if len(route) == len(tickets) + 1:
            return True
        
        for i in range(len(tickets)):
            start, end = tickets[i]
            
            if not visited[i] and start == current:
                visited[i] = True
                route.append(end)
                
                if dfs(end):
                    return True
                
                route.pop()
                visited[i] = False
        
        return False
    
    dfs(route[0])
    return route