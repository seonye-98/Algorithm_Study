//이진탐색 문제풀이2

//https://www.acmicpc.net/problem/10816
//난이도 : 실버4
//이진탐색

/*
숫자카드 N개 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지
N : 가지고 있는 숫자 카드의 개수
숫자 카드에 적혀있는 정수
M : 찾아야 할 카드의 개수
찾아야할 숫자 카드 정수

*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const cards = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
const M = Number(input[2]);
const find_cards = input[3].split(' ').map(Number);

function lowerBound(cards, target) {
  let start = 0;
  let end = cards.length;

  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (cards[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return end;
}

function upperBound(cards, target) {
  let start = 0;
  let end = cards.length;

  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (cards[mid] > target) end = mid;
    else start = mid + 1;
  }
  return end;
}

function countByRange(arr, leftValue, rightValue) {
  let rightIndex = upperBound(cards, rightValue);
  let leftIndex = lowerBound(cards, leftValue);
  return rightIndex - leftIndex;
}

let answer = [];

for (let i = 0; i < find_cards.length; i++) {
  let curr = find_cards[i];
  answer.push(countByRange(cards, curr, curr));
}

console.log(answer.join(' '));

//https://www.acmicpc.net/problem/18353
//난이도 : 실버2
//이진탐색, LIS

/*
병사 배치시 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
특정한 위치에 있는 병사는 열외, 그러면서도 남아있는 병사의 수가 최대
N : 병사 번호
각 병사의 전투력

LIS : Longest Increasing Subsequence 알고리즘
"가장 긴 증가하는 부분 수열"
부분 수열 : 주어진 수열의 일부 항을 원래 순서대로 나열하여 얻을 수 있는 수열

이진 탐색을 활용하면 최악의 경우 시간 복잡도 O(NlogN)의 코드로 해결
아이디어: 현재 원소가 가장 크다면 뒤에 삽입, 그렇지 않다면 최대한 왼쪽의 원소와 교체

*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const soldiers = input[1].split(' ').map(Number);

soldiers.reverse();

let d = [0]; //LIS 배열

function lowerBound(arr, target, start, end) {
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return end;
}

for (x of soldiers) {
  if (d[d.length - 1] < x) {
    d.push(x);
  } else {
    let index = lowerBound(d, x, 0, d.length);
    d[index] = x;
  }
}

console.log(N - (d.length - 1));

//https://www.acmicpc.net/problem/1300
//난이도 : 골드1
//이진탐색

/*
배열 NxN인 배열 A를 만들었다. A[i][j] = ixj,
이 수를 일차원 배열 B에 넣으면 B의 크기는 NxN가 된다.
B를 오름차순 정렬했을 때, B[k]를 구해보자
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const n = Number(input[0]);
const k = Number(input[1]);

let start = 1;
let end = 10 ** 10;

let result = 0;
while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0; //mid보다 작거나 같은 데이터의 개수
  for (let i = 1; i <= n; i++) {
    total += Math.min(parseInt(mid / i), n);
  }
  if (total >= k) {
    result = mid;
    end = mid - 1;
  } else start = mid + 1;
}
console.log(result);
