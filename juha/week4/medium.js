function solution(answers) {
  let answer = [];
  const m1 = [1, 2, 3, 4, 5];
  const m2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let s1 = 0;
  let s2 = 0;
  let s3 = 0;

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] == m1[i % m1.length]) {
      s1++;
    }
    if (answers[i] == m2[i % m2.length]) {
      s2++;
    }
    if (answers[i] == m3[i % m3.length]) {
      s3++;
    }
  }
  const max = Math.max(s1, s2, s3);

  const result = [];
  if (s1 == max) result.push(1);
  if (s2 == max) result.push(2);
  if (s3 == max) result.push(3);
  return result;
}
