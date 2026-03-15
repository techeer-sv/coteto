// 네트워크 (lv. 3)

// https://school.programmers.co.kr/learn/courses/30/lessons/43162

// 이코테 파이썬 첫 장 펴면 나오는 인접행렬을 이용한 그래프 탐색 유형과 거의 풀이법이 동일
// 암기하지않았다면 visited 와 같은 방문처할 배열을 선언해야겠다는 생각을 하기가 어려워서 lv3인 듯
function solution(n, computers) {
  var answer = 0;

  const visited = Array(n).fill(0);

  function dfs(i) {
    visited[i] = 1;
    console.log(visited);

    for (let j = 0; j < n; j++) {
      // 연결 & 방문X
      if (computers[i][j] === 1 && !visited[j]) {
        dfs(j);
      }
    }
  }

  /*
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    */
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer++;
      dfs(i);
    }
  }

  return answer; // 개수
}
