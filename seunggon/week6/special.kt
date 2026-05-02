// 네트워크 (lv. 3)

// https://school.programmers.co.kr/learn/courses/30/lessons/43162

class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        
        // A , B 직접 연결 B, C 직접 연결 -> A,c간접연결 = 같은 네트워크
        // 0이 1,2랑 직접 연결되어있어도, 2가 3이랑 추가로 연결되어있다면 [0][3] == 0 이어도 네트워크하나
        
        // val visited = mutableListOf<Int>()
        val visited = IntArray(n) // 크기 n의 [0,0,0,0...] 배열
        
        fun dfs(idx:Int) { // 연결된 모든 컴퓨터를 visited 배열을 바꾸고, 다음 걸 
            visited[idx] = 1

            for (next in 0 until n) {
                 // 방문한거면 dfs를 또 할필요는 없음. 이 조건만큼은 dfs를 최초 호출한 것과 같은 조건이 들어가있어야함
                if (computers[idx][next] == 1 && visited[next]==0) {
                    dfs(next)
                }   
            }   
        }
        
        
        for (i in 0 until n) {
            if (visited[i]==0) { // 컴퓨터 i가 방문 전이라면
                dfs(i)
                answer++ // count를 올리는 건 완전 새로운 dfs를 할 때만 수행
            }
        }
        
        return answer
    }

}