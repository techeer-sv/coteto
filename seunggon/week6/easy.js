// 콜라츠 추측 (lv. 1)

// https://school.programmers.co.kr/learn/courses/30/lessons/12943

/*
1이될때까지 반복 -> 1
num % 2 == 0 => /2
num % 2 != 0 => *3 +1

count
*/

function solution(num) {
  var answer = 0;

  // 입력이 1일 때는 아예 while을 돌지 않으므로 초깃값 0을 출력
  while (num != 1 && answer != 500) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num = num * 3 + 1;
    }

    answer++;
    console.log(answer);
  }

  return answer != 500 ? answer : -1;
}
