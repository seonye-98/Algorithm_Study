//JavaScript 입출력 문제 풀이
const path = require('path');
//https://www.acmicpc.net/problem/2557

console.log('Hello World!');

//https://www.acmicpc.net/problem/1000

const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', (line) => {
  let [A, B] = line.split(' ').map((d) => Number(d));
  console.log(A + B);
  rl.close();
  process.exit(0);
});
/*
//백준 input file을 읽어와서 풀기, 메모리 사용량이 낮고, 시간도 빠르다
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let line = input[0].split(' ');

let a = parseInt(line[0]);
let b = parseInt(line[1]);

console.log(a + b);
*/

//https://www.acmicpc.net/problem/10998

rl.on('line', (line) => {
  let [A, B] = line.split(' ').map((d) => Number(d));
  console.log(A * B);
  rl.close();
  process.exit(0);
});

//https://www.acmicpc.net/problem/10869

let fs = require('fs');
let input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .split('\n');

let [A, B] = input[0].split(' ');

['+', '-', '*', '/', '%'].forEach((op) => {
  let result = eval(A + op + B);
  if (op === '/') console.log(parseInt(result));
  else console.log(result);
});

//https://www.acmicpc.net/problem/2588

const [num1, num2] = input.map((value) => Number(value.trim()));

for (let i = 1; i < 4; i++) {
  console.log(num1 * parseInt((num2 % 10 ** i) / 10 ** (i - 1)));
}
//권장 풀이
/*
const [num1, num2] = input.map((value) => value.trim());

for (let i = 0; i < 3; i++) {
  console.log(Number(num1)*num2[i])
*/
console.log(num1 * num2);
