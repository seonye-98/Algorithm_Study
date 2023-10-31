//파라메트릭 서치 문제 풀이
//https://www.acmicpc.net/problem/2512
//난이도 : 실버2
/*
정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
2. 모든 요청이 배정될 수 없는 경우 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는
모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서 요청한 금액을 그대로 배정

변화되는 값 x는 상한액
상한액은 N부터 1,000,000,000 이하
f(x)는 단조 감소 함수

상한액을 1부터 예산요청 배열의 최대값까지 이진탐색을 통해 최적의 해를 찾는다.
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const arr = input[1].split(' ').map(Number);
const m = Number(input[2]);

let start = 1;
let end = arr.reduce((a, b) => Math.max(a, b));

let result = 0;

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0; //배정된 예산의 총액
  for (x of arr) {
    total += Math.min(mid, x);
  }
  if (total <= m) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);
