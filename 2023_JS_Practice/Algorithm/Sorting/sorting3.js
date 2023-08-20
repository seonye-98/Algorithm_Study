//정렬 문제 풀이3
//https://www.acmicpc.net/problem/18870
//크기순위
/*
const N = Number(input[0]);
let numArr = input[1].split(' ').map(Number);
let uniqueArr = [...new Set(numArr)];
uniqueArr.sort((a, b) => a - b);

let myMap = new Map();
uniqueArr.forEach((num, idx) => myMap.set(num, idx));

let answer = '';

numArr.forEach((num) => (answer += myMap.get(num) + ' '));
console.log(answer);
*/

//https://www.acmicpc.net/problem/10814
//Node.js 정렬은 기본적으로  stable 하므로 정렬기준이 같은 경우 index기준으로 sort하게 되어있음
/*
const N = Number(input[0]);
let members = [];

input.slice(1, N + 1).forEach((line, index) => {
  const data = line.split(' ');
  const [age, name] = [Number(data[0]), data[1].trim()];
  let member = {
    order: index,
    age,
    name,
  };
  members.push(member);
});

const compare = (a, b) => {
  if (a.age !== b.age) return a.age - b.age;
  return a.order - b.order;
};

members.sort(compare);

let result = '';

members.forEach((member) => {
  result += `${member.age} ${member.name}\n`;
});

console.log(result);
*/
//https://www.acmicpc.net/problem/1427

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');
/*
내풀이
const num = input[0].trim();
let arr = [];

for (let i = 0; i < num.length; i++) {
  arr.push(Number(num[i]));
}

arr.sort((a, b) => b - a);

console.log(arr.join(''));
*/
//빈도수로 풀이
let n = input[0].trim();
let cnt = Array(10).fill(0);

for (let x of n) {
  cnt[Number(x)]++;
}

let answer = '';

for (let i = 9; i >= 0; i--) {
  for (let j = 0; j < cnt[i]; j++) answer += i + '';
}

console.log(answer);
