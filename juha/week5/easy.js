function solution(n) {
  const a = 1234567;

  let f = [0, 1];
  for (let i = 2; i <= n; i++) {
    f[i] = (f[i - 1] + f[i - 2]) % a;
  }
  return f[n];
}
