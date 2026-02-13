function solution(rsp) {
  const win = {
    2: "0",
    0: "5",
    5: "2",
  };
  const Rsp = rsp.split("");
  const WinArray = Rsp.map((char) => {
    return win[char];
  });
  const answer = WinArray.join("");
  return answer;
}
