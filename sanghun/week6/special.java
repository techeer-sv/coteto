import java.util.*;

class Solution {
    public static boolean[] visited;
    public int solution(int n, int[][] computers) {
        int count = 0;
        visited = new boolean[n];
        
        for(int i=0; i<n; i++){
            if(visited[i] == false){
                bfs(i, computers);
                count++;
            }
        }
        
        return count;
    }
    
    public void bfs(int k, int[][] computers){
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(k);
        
        while(!queue.isEmpty()){
            int current = queue.poll();
            
            for(int i=0; i<computers[0].length; i++){
                if(computers[current][i] == 1 && visited[i] == false){
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}
