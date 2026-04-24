// 의상 (Lv.2)
// https://school.programmers.co.kr/learn/courses/30/lessons/42578

function solution(clothes) {
  // 최소 1개는 입음
  // [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
  // 종류로는 2 1가지
  // 하지만 안입는거까지해서 각각의 인덱스를 0,1,2로 두면
  // 0:안입는다. 1 : 1번 옷, 2: 2번 옷
  // (0,1,2) (0,1) => 3*2 -1 => 5가지
  // (0,1,2,3) - 1(0.0)  => 3가지
  // (0,1) (0, 1) (0,1)
  // 2*2*2 - 1 = 7가
  // a,b,c, ab, ac,bc,abc

  // 순열 조합 문제느낌
  const countByKind = {};

  for (const [name, kind] of clothes) {
    if (countByKind[kind] == undefined) {
      countByKind[kind] = 1;
    } else {
      countByKind[kind] += 1;
    }
  }

  let answer = 1;

  for (const kind in countByKind) {
    // 여긴 [kind,count] of 아님
    answer *= countByKind[kind] + 1; // 2개여도 (0,1,2)로 3가지, 1개여도 (0,1) 로 2가지
  }

  // 0,0 빼는 건 이미처리
  return answer - 1;
}
