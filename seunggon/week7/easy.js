// Lv2. 게임 맵 최단거리
// (bfs)
// https://school.programmers.co.kr/learn/courses/30/lessons/1844

// 풀이 1. 지나온 칸에 거리를 더해버리기 (띄어쓰기나 주석을 변경하다보면 효율성 테스트에서 테스트3가 가끔 시간 초과함)
function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = [[0, 0]];

  while (queue.length > 0) {
    const [x, y] = queue.shift();

    if (x === n - 1 && y === m - 1) {
      return maps[x][y];
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] === 1) {
        maps[nx][ny] = maps[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }

  return -1;
}

// 풀이 2. 풀이1 방식에 .shift() 대신 front 변수 사용
function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = [[0, 0]];
  let front = 0;

  while (front < queue.length) {
    // queue.length : 넣은 개수.
    const [x, y] = queue[front++]; // 현재 front의 것을 가져오고 ++

    if (x === n - 1 && y === m - 1) {
      return maps[x][y];
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1) {
        maps[nx][ny] = maps[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }

  return -1;
}

// 풀이 3. Queue를 선언
class Queue {
  //  배열에서 원소를 실제로 제거하지 않고, front/rear 인덱스만 움직이는 방식 (배열을 줄이지 않음)
  items = [];
  front = 0; // 다음에 꺼낼 위치
  rear = 0; // 다음 원소가 '들어갈' 위치

  push(item) {
    this.items.push(item);
    this.rear++;
  }

  first() {
    return this.items[this.front];
  }

  last() {
    return this.items[this.rear - 1]; // rear - 1을 해야 마지막 인덱스
  }

  pop() {
    return this.items[this.front++]; // 현재 front 위치에있는 원소를 반환하고 front의 인덱스를 +1
  }

  isEmpty() {
    return this.front == this.rear;
  }
}
