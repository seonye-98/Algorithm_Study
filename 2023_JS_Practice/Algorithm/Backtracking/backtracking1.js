//백트래킹 문제풀이1

//https://www.acmicpc.net/problem/15649
//난이도 : 실버3
//백트래킹, 경우의 수, 완전 탐색
/*
자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중 중복없이 M개를 고른 수열을 구하는 프로그램
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);

let result = [];

function permutation(arr) {
  if (arr.length === M) result.push(arr.join(' '));
  for (let i = 1; i <= N; i++) {
    if (!arr.includes(i)) {
      permutation([...arr, i]);
    }
  }
}

permutation([]);

console.log(result.join('\n'));

//https://www.acmicpc.net/problem/10974
//난이도 : 실버3
//백트래킹, 경우의 수, 완전 탐색
/*
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);

let result = [];

function permutation(arr) {
  if (arr.length === N) result.push(arr.join(' '));
  for (let i = 1; i <= N; i++) {
    if (!arr.includes(i)) {
      permutation([...arr, i]);
    }
  }
}

permutation([]);

console.log(result.join('\n'));

//https://www.acmicpc.net/problem/7490
//난이도 : 골드5
//백트래킹, 경우의 수, 완전 탐색
/*
1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각
그리고 +나 -또는 공백을 숫자 사이에 삽입
이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지 살피자
N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램 작성

중복 순열
*/
const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const t = Number(input[0]);
const arr = input.splice(1, t).map((n) => Number(n.trim()));

const opt = [' ', '+', '-'];

function isPossible(test_case, n) {
  let evalStr = '';

  for (let i = 0; i < test_case.length; i++) {
    evalStr += `${i + 1}${test_case[i]}`;
  }
  evalStr += n;

  return [evalStr, eval(evalStr.split(' ').join(''))];
}

function bfs(arr, n) {
  let result = [];
  function permutationWithRepeat(arr) {
    if (arr.length === n - 1) {
      const [str, evalValue] = isPossible(arr, n);
      if (evalValue === 0) result.push(str.trim());
      return;
    }
    for (let i = 0; i < 3; i++) {
      permutationWithRepeat([...arr, opt[i]]);
    }
  }
  permutationWithRepeat(arr);
  return result;
}
let answer = [];
for (let i = 0; i < t; i++) {
  let cases = bfs([], arr[i]);
  answer.push([...cases].join('\n'));
}

console.log(answer.join('\n\n'));
