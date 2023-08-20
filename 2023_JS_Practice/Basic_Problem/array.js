const path = require('path');
//배열 문제 풀이
//https://www.acmicpc.net/problem/10818
/*
const N = Number(input[0]);
const numArr = input[1].split(' ').map(Number);
let min = numArr.reduce((a, b) => Math.min(a, b));
let max = numArr.reduce((a, b) => Math.max(a, b));

console.log(min, max);

let minValue = 1000001;
let maxValue = -1000001;
for (let i = 0; i < N; i++) {
  if (minValue > numArr[i]) minValue = numArr[i];
  if (maxValue < numArr[i]) maxValue = numArr[i];
}
console.log(minValue, maxValue);
*/
//https://www.acmicpc.net/problem/2562
/*
const numArr = input.map(Number);

let maxVal = -1;
let maxIdx = 0;
for (let i = 0; i < numArr.length; i++) {
  if (maxVal < numArr[i]) {
    maxVal = numArr[i];
    maxIdx = i + 1;
  }
}
console.log(maxVal + '\n' + maxIdx);
*/
//https://www.acmicpc.net/problem/3052
/*
const numArr = input.map(Number);
let resultSet = new Set();

numArr.forEach((num) => {
  resultSet.add(num % 42);
});

console.log(resultSet.size);
*/
//https://www.acmicpc.net/problem/4344
/*
const N = Number(input[0]);
let result = '';
for (let i = 0; i < N; i++) {
  let [student, ...score] = input[i + 1].split(' ').map(Number);
  let scoreSum = score.reduce((a, b) => a + b, 0);
  let averageScore = scoreSum / student;
  let greatStudent = score.filter((score) => score > averageScore);
  let percentage = (greatStudent.length / student) * 100;
  result += `${percentage.toFixed(3)}%\n`;
}

console.log(result);
*/
//https://www.acmicpc.net/problem/1546

const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const scoreArr = input[1].split(' ').map(Number);

const calNewScore = (scoreArr) => {
  const M = scoreArr.reduce((a, b) => Math.max(a, b), 0);
  let newScoreArr = scoreArr.map((score) => (score / M) * 100);
  let newScoreSum = newScoreArr.reduce((a, b) => a + b, 0);
  return parseFloat(newScoreSum / N);
};

console.log(calNewScore(scoreArr));
