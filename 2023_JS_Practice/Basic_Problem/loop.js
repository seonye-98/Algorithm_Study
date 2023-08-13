const path = require('path');
//반복문 문제 풀이
//https://www.acmicpc.net/problem/8393
/*
const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = 0;

rl.on('line', (line) => {
  n = Number(line);
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  console.log(sum);

  //등차 수열의 합
  let result = (n * (1 + n)) / 2;
  console.log(result);

  rl.close();
});
*/
//https://www.acmicpc.net/problem/2739
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

const n = Number(input[0]);

for (let i = 1; i <= 9; i++) {
  console.log(`${n} * ${i} = ${n * i}`);
}
*/
//https://www.acmicpc.net/problem/2438
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

const n = Number(input[0]);
for (let i = 1; i <= n; i++) {
  console.log('*'.repeat(i));
}
//이중반복문 사용
let result = '';
for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= i; j++) {
    result += '*';
  }
  result += '\n';
}
console.log(result);
*/
//https://www.acmicpc.net/problem/15552
//빠른 A+B

const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');
const N = Number(input[0]);

let result = '';
for (let i = 1; i <= N; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  result += a + b + '\n';
}
console.log(result);
