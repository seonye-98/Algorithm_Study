//https://www.acmicpc.net/problem/19939
/*
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');

let [N, K] = input[0].split(' ').map(Number);

const min = (K ** 2 - K) / 2;

if (N - min < K) console.log(-1);
else {
  let left = (N - min) % K;
  if (left === 0) console.log(K - 1);
  else console.log(K);
}
*/
//https://www.acmicpc.net/problem/17609
/*
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');

const T = Number(input[0]);

function palindrome(x) {
  return x === x.split('').reverse().join('');
}

for (let testCase = 1; testCase < T + 1; testCase++) {
  let word = input[testCase].trim();
  if (palindrome(word)) console.log(0);
  else {
    let found = false;
    let n = word.length;
    for (let i = 0; i < parseInt(n / 2); i++) {
      if (word[i] !== word[n - i - 1]) {
        if (palindrome(word.slice(0, i) + word.slice(i + 1, n))) found = true;
        if (palindrome(word.slice(0, n - i - 1) + word.slice(n - i, n)))
          found = true;
        break;
      }
    }
    if (found) console.log(1);
    else console.log(2);
  }
}
*/
//https://www.acmicpc.net/problem/1493
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');
/*
const [l, w, h] = input[0].split(' ').map(Number);
const T = Number(input[1]);
let cubes = [];
for (let i = 2; i < 2 + T; i++) {
  let [type, cnt] = input[i].split(' ').map(Number);
  let size = 2 ** type;
  let volume = size ** 3;
  cubes.push([volume, cnt]);
}

let answer = 0;
let totalVolume = l * w * h;
console.log(totalVolume, cubes);
while (totalVolume > 0 && cubes.length > 0) {
  let [volume, cnt] = cubes.pop();
  for (let j = cnt; j > -1; j--) {
    if (totalVolume >= volume * j) {
      cnt = j;
      break;
    }
  }
  answer += cnt;
  totalVolume -= volume * cnt;
  console.log(volume, cnt, volume * cnt, totalVolume);

}

if (totalVolume > 0) console.log(-1);
else console.log(answer);
*/
function nearestSquare(x) {
  let i = 1;
  while (2 ** i <= x) i += 1;
  return i - 1;
}
let [length, width, height] = input[0].split(' ').map(Number);
let cubes = Array(20).fill(0);

let n = Number(input[1]);
for (let i = 2; i <= n + 1; i++) {
  let [a, b] = input[i].split(' ').map(Number);
  cubes[a] = b;
}

let size = nearestSquare(
  [length, width, height].reduce((a, b) => Math.min(a, b), 1000000)
);
let res = 0;
let used = 0;

for (let i = size; i >= 0; i--) {
  used *= 8;
  cur = 2 ** i;
  console.log('used, cur', used, cur);
  let required =
    parseInt(length / cur) * parseInt(width / cur) * parseInt(height / cur) -
    used;
  let usage = Math.min(required, cubes[i]);
  console.log('required, usage', required, usage);
  res += usage;
  used += usage;
  console.log('res, used', res, used);
  console.log('------------------------');
}
if (used === length * width * height) console.log(res);
else console.log(-1);
