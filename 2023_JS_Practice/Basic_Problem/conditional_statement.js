const path = require('path');
//조건문 문제 풀이
//https://www.acmicpc.net/problem/9498

const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString();

const score = Number(input.trim());

if (score >= 90) console.log('A');
else if (score >= 80) console.log('B');
else if (score >= 70) console.log('C');
else if (score >= 60) console.log('D');
else console.log('F');

//https://www.acmicpc.net/problem/2884

//const fs = require('fs');
const _input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

let [H, M] = _input[0].split(' ').map((time) => Number(time));

if (M < 45) {
  H -= 1;
  M += 15;
  if (H < 0) H = 23;
} else M -= 45;

console.log(`${H} ${M}`);

//https://www.acmicpc.net/problem/2525

//const fs = require('fs');
const input1 = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

let [A, B] = input1[0].split(' ').map((time) => Number(time.trim()));
const C = Number(input1[1]);

if (B + C > 59) {
  const cookHour = parseInt((B + C) / 60);
  const cookMin = (B + C) % 60;
  A += cookHour;
  B = cookMin;
  if (A > 23) A -= 24;
} else B += C;

console.log(`${A} ${B}`);

//애초에 현재시각을 분으로 바꾸는 것이 더 쉬울수 있다.

//https://www.acmicpc.net/problem/2480

//const fs = require('fs');
const input2 = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

const [_A, _B, _C] = input2[0].split(' ').map(Number);
let price = 0;

if (_A === _B && _B === _C) price = 10000 + _A * 1000;
else if (_A === _B || _A === _C) price = 1000 + _A * 100;
else if (_B === C) price = 1000 + _B * 100;
else price = Math.max(_A, _B, _C) * 100;

console.log(price);
