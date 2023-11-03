//백트래킹 문제풀이2

//https://www.acmicpc.net/problem/15650
//난이도 : 실버3
//백트래킹, 경우의 수, 완전 탐색

/*
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
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
      if (arr.length === 0) permutation([...arr, i]);
      else if (arr.length > 0 && arr.at(-1) < i) {
        permutation([...arr, i]);
      }
    }
  }
}

permutation([]);

console.log(result.join('\n'));

//https://www.acmicpc.net/problem/15651
//난이도 : 실버3
//백트래킹, 경우의 수, 완전 탐색

/*
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);

let result = [];

function permutationWithRepeat(arr) {
  if (arr.length === M) {
    result.push(arr.join(' '));
    return;
  }
  for (let i = 1; i <= N; i++) {
    permutationWithRepeat([...arr, i]);
  }
}

permutationWithRepeat([]);

console.log(result.join('\n'));

//https://www.acmicpc.net/problem/15651
//난이도 : 실버3
//백트래킹, 경우의 수, 완전 탐색

/*
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다. -> 같거나 큰 오름차순
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);

let result = [];

function permutationWithRepeat(arr) {
  if (arr.length === M) {
    result.push(arr.join(' '));
    return;
  }
  for (let i = 1; i <= N; i++) {
    if (arr.length === 0) permutationWithRepeat([...arr, i]);
    else if (arr.at(-1) <= i) {
      permutationWithRepeat([...arr, i]);
    }
  }
}

permutationWithRepeat([]);

console.log(result.join('\n'));
