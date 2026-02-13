function solution(lottos, win_nums) {
  const zero = lottos.filter((num) => num == 0).length;
  const match = lottos.filter((num) => win_nums.includes(num)).length;
  const rank = [6, 6, 5, 4, 3, 2, 1];
  const maxRank = rank[match + zero];
  const minRank = rank[match];

  return [maxRank, minRank];
}
