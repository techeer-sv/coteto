// 단어 변환 (Lv. 3)

// https://school.programmers.co.kr/learn/courses/30/lessons/43163

function solution(begin, target, words) {
  if (!words.includes(target)) {
    return 0;
  }

  const queue = [[begin, 0]];
  const visited = new Set([begin]);

  while (queue.length > 0) {
    const [current, count] = queue.shift();

    if (current === target) return count;

    for (const word of words) {
      if (!visited.has(word) && isConvertible(current, word)) {
        visited.add(word);
        queue.push([word, count + 1]);
      }
    }
  }

  return 0;
}

function isConvertible(word1, word2) {
  let count = 0;
  for (let i = 0; i < word1.length; i++) {
    if (word1[i] !== word2[i]) count++;
    if (count > 1) return false;
  }
  return count === 1;
}
