//https://www.acmicpc.net/problem/13305

/*
58점
const N = Number(input[0]);
const road = input[1].split(' ').map(Number);
const cost = input[2].split(' ').map(Number);
let total_road = road.reduce((a, b) => a + b, 0);
let min_cost = cost.slice(0, -1).reduce((a, b) => Math.min(a, b), 10000);

let total_cost = 0;
let i = 0;

while (i < N - 1) {
  let curr_cost = cost[i];
  let find = i;
  let sum_road = 0;
  if (curr_cost === min_cost) {
    total_cost += curr_cost * total_road;
    break;
  }
  for (let j = i + 1; j < N; j++) {
    if (cost[j] < curr_cost) {
      find = j - 1;
      break;
    }
  }

  sum_road = road.slice(i, find + 1).reduce((a, b) => a + b, 0);
  total_cost += curr_cost * sum_road;

  total_road -= sum_road;
  if (i === find) i += 1;
  else i += find - i + 1;
}

console.log(total_cost);

//정해코드
const n = Number(input[0]);
let dist = input[1].split(' ').map(Number);
let cost = input[2].split(' ').map(Number);

//[5,2,4,1] => [5,2,2,1]
let minCost = cost[0];
for (let i = 0; i < n; i++) {
  minCost = Math.min(minCost, cost[i]);
  cost[i] = minCost;
}

let answer = BigInt(0);
for (let i = 0; i < n - 1; i++) {
  //JavaScript에서 큰 정수를 처리할 때 BigInt 사용
  answer += BigInt(dist[i]) * BigInt(cost[i]);
}
console.log(String(answer));

*/
//https://www.acmicpc.net/problem/1931
/*
const N = Number(input[0]);
let info = input.slice(1, N + 1).map((i) => i.split(' ').map(Number));

const compare = (a, b) => {
  if (a[1] !== b[1]) return a[1] - b[1];
  else return a[0] - b[0];
};

info.sort(compare);

let cnt = 1,
  cur = 0;

for (let i = 1; i < N; i++) {
  if (info[cur][1] <= info[i][0]) {
    cur = i;
    cnt += 1;
  }
}
console.log(cnt);
*/

//https://www.acmicpc.net/problem/11509
/*
const N = Number(input[0]);
const h = input[1].split(' ').map(Number);
let result = 0;
let arrow = new Array(1000001).fill(0); //각 높이 화살 개수
for (let x of h) {
  if (arrow[x] > 0) {
    arrow[x] -= 1;
    arrow[x - 1] += 1;
  } else {
    arrow[x - 1] += 1;
    result += 1;
  }
}

console.log(result);
*/

//https://www.acmicpc.net/problem/9009
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');
