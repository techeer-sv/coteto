function solution(babbling) {
  const wordList = ["aya", "ye", "woo", "ma"];
  let count = 0;

  for (let babbel of babbling) {
    let valid = true;

    for (let s of wordList) {
      if (babbel.includes(s + s)) {
        valid = false;
        break;
      }
    }

    if (!valid) continue;

    let currentWord = babbel;
    for (let s of wordList) {
      currentWord = currentWord.split(s).join(" ");
    }

    if (currentWord.trim().length === 0) {
      count++;
    }
  }

  return count;
}
