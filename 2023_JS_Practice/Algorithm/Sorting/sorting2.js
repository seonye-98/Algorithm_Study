//정렬 문제 풀이2
//https://www.acmicpc.net/problem/11650
/*
const N = Number(input[0]);
const pointArr = input.slice(1, N + 1).map((item) =>
  item
    .trim()
    .split(' ')
    .map((item) => Number(item))
);

const compare = (a, b) => {
  if (a[0] === b[0]) return a[1] - b[1];
  return a[0] - b[0];
};

pointArr.sort(compare);

let result = '';

pointArr.forEach((item) => {
  result += item.join(' ') + '\n';
});

console.log(result);
*/

//https://www.acmicpc.net/problem/11651
/*
const N = Number(input[0]);
const pointArr = input.slice(1, N + 1).map((item) =>
  item
    .trim()
    .split(' ')
    .map((item) => Number(item))
);

const compare = (a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
};

pointArr.sort(compare);

let result = '';

pointArr.forEach((item) => {
  result += item.join(' ') + '\n';
});

console.log(result);
*/
//https://www.acmicpc.net/problem/1181

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

const N = Number(input[0]);
let wordArr = new Set(input.slice(1, N + 1).map((item) => item.trim()));

const compare = (a, b) => {
  if (a.length === b.length) return a.localeCompare(b);
  return a.length - b.length;
};

wordArr = [...wordArr].sort(compare);

console.log(wordArr.join('\n'));
