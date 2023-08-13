const path = require('path');
//문자열 문제 풀이
//https://www.acmicpc.net/problem/11720
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const stringNum = input[1];
let sum = 0;
for (x of stringNum) {
  sum += Number(x);
}
console.log(sum);
*/

//https://www.acmicpc.net/problem/2675
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
let result = '';
for (let i = 1; i <= N; i++) {
  const [num, string] = input[i].split(' ');
  for (x of string) {
    result += x.repeat(Number(num));
  }
  result += '\n';
}

console.log(result);
*/
//https://www.acmicpc.net/problem/2908
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const orgNum = input[0].split(' ');

const revNum = orgNum.map((x) => Number(x.split('').reverse().join('')));

console.log(Math.max(...revNum));
*/
//https://www.acmicpc.net/problem/1316
/*
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);

const groupCheck = (string) => {
  let wordSet = new Set(string.trim().charAt(0));
  for (let i = 0; i < string.length - 1; i++) {
    if (string[i] != string[i + 1]) {
      if (wordSet.has(string[i + 1])) return false;
      else wordSet.add(string[i + 1]);
    }
  }
  return true;
};
let result = [];
for (let i = 1; i <= N; i++) {
  result.push(groupCheck(input[i]));
}
result = result.filter((x) => x === true);
console.log(result.length);
*/
//https://www.acmicpc.net/problem/1152

const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

let data = input[0].trim().split(' ');

if (data == '') console.log(0);
else console.log(data.length);
