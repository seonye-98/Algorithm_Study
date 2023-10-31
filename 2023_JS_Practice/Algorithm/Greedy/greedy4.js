//https://www.acmicpc.net/problem/19939
/*
let [N, K] = input[0].split(' ').map(Number);

// 0 ~ K - 1 , (K^2 - K) /2
const min = (K ** 2 - K) / 2;

if (N - min < K) console.log(-1);
else {
  let left = (N - min) % K;
  if (left === 0) console.log(K - 1);
  else console.log(K);
}
//20 4 -> 4 ( 3 4 6 7 )
//72 8 -> 8 ( 5 6 7 8 10 11 12 13 )
*/
//https://www.acmicpc.net/problem/17609
/*
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
5
abcddadca 2
ppbpppb 2
aabcdeddcba 2
aabab 2 
aapqbcbqpqaa 1
*/
//https://www.acmicpc.net/problem/1493
const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const [lenght, width, height] = input[0].split(' ').map(Number);
const tc = Number(input[1]);
let box = [];
for (let i = 2; i < 2 + tc; i++) {
  const [size, cnt] = input[i].split(' ').map(Number);
  box.push([2 ** size, cnt]);
}
box.sort((a, b) => b[0] - a[0]);
console.log(lenght, width, height);
console.log(box);
