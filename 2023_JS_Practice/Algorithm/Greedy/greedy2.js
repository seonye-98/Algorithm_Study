//https://www.acmicpc.net/problem/2839
/*
let N = Number(input[0]);
let total = 0;
let maxFive = parseInt(N / 5);

for (let i = maxFive; i >= 0; i--) {
  let left = N - 5 * i;
  if (left % 3 !== 0) continue;
  else {
    total += i + left / 3;
    break;
  }
}

if (total === 0) total = -1;

console.log(total);
*/
//https://www.acmicpc.net/problem/16953
/*
let [A, B] = input[0].split(' ').map(Number);
let cnt = 1;
while (B !== A && A < B) {
  if (B % 2 !== 0) {
    B = B.toString();
    let b_size = B.toString().length;
    if (B[b_size - 1] === '1') B = Number(B.slice(0, b_size - 1));
    else break;
  } else B /= 2;
  cnt += 1;
}

if (B !== A) cnt = -1;

console.log(cnt);
*/
//https://www.acmicpc.net/problem/1789
/*
let S = Number(input[0]);
let n = parseInt(S ** (1 / 2));
S -= (n * (n + 1)) / 2;

if (S >= n + 1 && S !== 0) n++;

while (S - n > 0) {
  if (S - n < n + 1) {
    break;
  }
  S -= n;
  n++;
}
console.log(n);

//정해 코드
let sum = 0;
let current = 0;
while (sum <= s) {
  current += 1;
  sum += current;
}
console.log(current - 1);
*/
//https://www.acmicpc.net/problem/1946
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');
const T = Number(input[0]);
let index = 1;

for (let tc = 0; tc < T; tc++) {
  const N = Number(input[index++]);
  const apply = input
    .slice(index, index + N)
    .map((score) => score.trim().split(' ').map(Number));
  index += N;
  apply.sort((a, b) => a[0] - b[0]);
  let count = 0;
  let minVal = N;
  for (let i = 0; i < N; i++) {
    if (i === 0) {
      count += 1;
      minVal = apply[i][1];
      continue;
    }
    if (apply[i][1] < minVal) {
      count += 1;
      minVal = Math.min(minVal, apply[i][1]);
    }
  }

  console.log(count);
}
