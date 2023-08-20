//정렬 문제 풀이1
//https://www.acmicpc.net/problem/2752

/*
const numArr = input[0].trim().split(' ').map(Number);
numArr.sort((a, b) => a - b);
console.log(numArr.join(' '));
*/

//https://www.acmicpc.net/problem/2750
//https://www.acmicpc.net/problem/2751
//sort() 메소드의 시간복잡도가 O(NlogN)이므로, 두 문제의 풀이는 같다.
/*
const N = Number(input[0].trim());
let numArr = input.slice(1, N + 1).map((num) => Number(num));

numArr.sort((a, b) => a - b);

console.log(numArr.join('\n'));
*/

//https://www.acmicpc.net/problem/11004

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().split('\n');

const [N, K] = input[0].trim().split(' ').map(Number);
const numArr = input[1].trim().split(' ').map(Number);
numArr.sort((a, b) => a - b);
console.log(numArr[K - 1]);
