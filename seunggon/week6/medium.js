// 타겟 넘버 (lv. 2)

// https://school.programmers.co.kr/learn/courses/30/lessons/43165

/*
numbers에는 n 개의 0이상의 정수
+ 혹은 -로 (op) target에 도달하는 방법의 수
*/

// except
// [] 0 이 들어오는 경우
function solution(numbers, target) {
  var answer = 0;

  // var index = 0;
  // var sum = 0;

  function dfs(idx, sum, numbers, target) {
    // 마지막까지 가기 전까진 return은 계속 하위에서 나온 결과들을 합친 것이 된다. 그래야 target과 일치할 때마다 방법 수가 1씩 더해진다.
    // 결국 마지막엔 1 혹은 0을 return한다.
    if (idx === numbers.length) {
      return sum === target ? 1 : 0;
    }

    return (
      dfs(idx + 1, sum + numbers[idx], numbers, target) +
      dfs(idx + 1, sum - numbers[idx], numbers, target)
    );
  }

  answer = dfs(0, 0, numbers, target);

  return answer;
}
