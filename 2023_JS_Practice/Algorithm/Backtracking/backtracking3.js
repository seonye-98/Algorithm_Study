//백트래킹 문제풀이3

//https://www.acmicpc.net/problem/10971
//난이도 : 실버2
//백트래킹, 경우의 수, 완전 탐색

/*
1부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에 길이있다.

한 외판원이 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로 계획, 한번 갔던 도시로는 다시 갈 수 없다.

가장 적은 비용을 들이는 여행 계획을 세우고자 한다.
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
i에서 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다.
W[i][i]는 항상 0이다. W[i][j] = 0 인 경우 i에서 j로 갈 수 없다.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성

N : 도시의 수
N개의 줄에는 비용 행렬이 주어진다.
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const n = Number(input[0]);
const price = input.splice(1, n).map((row) => row.trim().split(' ').map(Number));

const cities = [];
for (let i = 0; i < n; i++) cities.push(i);

function checkPrice(arr) {
  let total = 0;
  for (let i = 0; i < n; i++) {
    const [arrive, goal] = [...arr].splice(i, 2);

    total += price[arrive][goal];
  }
  return total;
}

let answer = Infinity;

function bfs(arr) {
  if (arr.length === n && price[arr.at(-1)][0] !== 0) {
    arr.push(arr[0]);
    answer = Math.min(answer, checkPrice(arr));

    return;
  }
  for (let i = 1; i < n; i++) {
    if (!price[arr.at(-1)][i]) continue;
    if (!arr.includes(i)) {
      bfs([...arr, i]);
    }
  }
}

bfs([0]);

console.log(answer);

//https://www.acmicpc.net/problem/2961
//난이도 : 실버2
//백트래킹, 경우의 수, 완전 탐색

/*
N개의 재료, 신맛 S와 쓴맛 B를 알고 있다.
음식 = 신맛의 곱, 쓴맛의 합
신맛과 쓴맛의 차이를 작게 만들려한다.
재료는 적어도 하나
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const n = Number(input[0]);
const foods = input.splice(1, n).map((food) => food.split(' ').map(Number));
const index = [];
for (let i = 0; i < n; i++) index.push(i);

let result = [];
let answer = Infinity;
function combination(arr, depth, len) {
  if (arr.length === len) {
    result.push(arr);
    let taste1 = 1;
    let taste2 = 0;
    for (let j = 0; j < arr.length; j++) {
      const [t1, t2] = foods[arr[j]];
      taste1 *= t1;
      taste2 += t2;
    }
    answer = Math.min(answer, Math.abs(taste1 - taste2));

    return;
  }
  for (let i = depth; i < index.length; i++) {
    if (!arr.includes(i)) combination([...arr, i], depth + 1, len);
  }
}

for (let i = 1; i < n + 1; i++) {
  combination([], 0, i);
}

console.log(answer);

//https://www.acmicpc.net/problem/6603
//난이도 : 실버2
//백트래킹, 경우의 수, 완전 탐색

/*
49가지 수 중 k개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택
kC6 계산하면됨
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const n = 6;
function combination(numbers) {
  let result = [];
  function generate(arr, depth) {
    if (arr.length === n) {
      result.push(arr.join(' '));
      return;
    }
    for (let i = depth; i < numbers.length; i++) {
      generate([...arr, numbers[i]], i + 1);
    }
  }
  generate([], 0);
  return result;
}
let answer = [];

for (let i = 0; i < input.length - 1; i++) {
  const [k, ...numbers] = input[i].split(' ').map(Number);
  answer.push(combination(numbers).join('\n'));
}
console.log(answer.join('\n\n'));
