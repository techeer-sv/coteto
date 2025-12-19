function solution(clothes) {
  let closet = {};
  for (let item of clothes) {
    let name = item[0];
    let type = item[1];

    if (closet[type]) {
      closet[type] += 1;
    } else {
      closet[type] = 1;
    }
  }
  let answer = 1;
  for (let type in closet) {
    answer = answer * (closet[type] + 1);
  }
  return answer - 1;
}
