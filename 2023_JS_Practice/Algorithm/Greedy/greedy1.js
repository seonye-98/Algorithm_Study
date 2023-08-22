// 그리디 문제 풀이1
//https://www.acmicpc.net/problem/11047
/*
let [N, K] = input[0].split(' ').map(Number);
const coins = input.slice(1, N + 1).map(Number);

coins.sort((a, b) => b - a);

let result = 0;

for (let coin of coins) {
  if (K === 0) break;
  if (coin <= K) {
    let count = parseInt(K / coin);
    K %= coin;
    result += count;
  }
}

console.log(result);
*/

//https://www.acmicpc.net/problem/11399
/*
const N = Number(input[0]);
const times = input[1].split(' ').map(Number);

times.sort((a, b) => a - b);

let total_time = [];

for (let i = 0; i < N; i++) {
  if (i === 0) total_time.push(times[i]);
  else {
    total_time.push(total_time[i - 1] + times[i]);
  }
}

let result = total_time.reduce((a, b) => a + b, 0);

console.log(result);
*/
//https://www.acmicpc.net/problem/1541
/*
+를 모두 -로 바꿔주기 위해서 -를 기준으로 split한 다음 괄호로 묶어주면 된다.
괄호로 묶어주는 이유? -(50+40) -> -50-40
*/

const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');

// 0으로 시작하는 수를 8진법 수로 처리하려고 시도
// 따라서, 0으로 시작하는 숫자문자열 처리

let exp = input[0]
  .replace(/^0+/g, '')
  .replace(/-0+/g, '-')
  .replace(/\+0+/g, '+');

let minusSplit = exp.split('-').map((Exp) => {
  return '(' + Exp + ')';
});
console.log(eval(minusSplit.join('-')));
