// week1_easy: 폰켓몬
// https://school.programmers.co.kr/learn/courses/30/lessons/1845

function solution(nums) {
  const inputSet = new Set(nums);
  // 중복없앤 게 배열길이 절반 이상이거나 더 적거나

  if (inputSet.size >= nums.length / 2) {
    return nums.length / 2;
  } else {
    return inputSet.size;
  }
}
