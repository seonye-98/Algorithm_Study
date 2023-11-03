//백트래킹 문제풀이3

//https://www.acmicpc.net/problem/9663
//난이도 : 골드4
//백트래킹, 경우의 수, 완전 탐색

/*
 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
 같은 열에 퀸을 놓을 수 없으므로, 각 행마다 몇번째 열에 넣을지 기록하는 1차원 배열만 있어도 된다.

*/

// const path = require('path');
// const fs = require('fs');
// const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

// const n = Number(input[0]);

// const row = new Array(n).fill(0);

// let cnt = 0;

// function possible(x) {
//   for (let i = 0; i < x; i++) {
//     if (row[x] === row[i]) return false;
//     if (Math.abs(row[x] - row[i]) === x - i) return false;
//   }
//   return true;
// }

// function dfs(x) {
//   if (x === n) {
//     cnt += 1;
//     return;
//   }

//   for (let i = 0; i < n; i++) {
//     row[x] = i;
//     if (possible(x)) dfs(x + 1);
//   }
// }

// dfs(0);

// console.log(cnt);

//https://www.acmicpc.net/problem/1987
//난이도 : 골드4
//백트래킹, 경우의 수, 완전 탐색

/*
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에 대문자 알파벳이 하나씩 적혀있음
좌측 상단 칸 (1행 1열)에는 말이 놓여있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀있는 알파벳은 
지금까지 지나온 모든 칸에 적혀있는 알파벳과 달라야 한다.
좌측 상단에서 시작해서, 말이 최대 몇 칸을 지날 수 있는지 구해라

배열로 하는 경우 시간초과
*/

// const path = require('path');
// const fs = require('fs');
// const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

// const [R, C] = input[0].split(' ').map(Number);
// const board = input.splice(1, R).map((r) => r.trim().split(''));

// const dx = [0, 1, 0, -1];
// const dy = [-1, 0, 1, 0];

// function check(x, y) {
//   if (x < 0 || x >= C || y < 0 || y >= R) return false;
//   return true;
// }

// let answer = 0;
// let arr = new Set([board[0][0]]);

// function dfs(depth, x, y) {
//   answer = Math.max(answer, depth);

//   for (let i = 0; i < 4; i++) {
//     let _x = x + dx[i];
//     let _y = y + dy[i];
//     if (!check(_x, _y)) continue;

//     if (!arr.has(board[_y][_x])) {
//       arr.add(board[_y][_x]);
//       dfs(depth + 1, _x, _y);
//       arr.delete(board[_y][_x]);
//     }
//   }
// }

// dfs(1, 0, 0);
// console.log(answer);

//https://www.acmicpc.net/problem/2529
//난이도 : 실버1
//백트래킹, 경우의 수, 완전 탐색

/*
부등호 기호 앞뒤에 서로 다른 한 자리 숫자를 넣어 모든 부등호 관계를 만족시키려고 한다.
0-9까지 숫자중에 k만큼 뽑아 나열할 수 있는 경우의 수인 순열을 모두 구해서 부등호를 모두 만족하는지 확인
-> 시간 초과

배열에 넣기 전에 부등호 만족하는지 체크해야함
*/

const path = require('path');
const fs = require('fs');
const { deflateSync } = require('zlib');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const k = Number(input[0]);
const signs = input[1].split(' ');

let maxNum = String(Number.MIN_SAFE_INTEGER);
let minNum = String(Number.MAX_SAFE_INTEGER);

function deflateSync(arr) {
  if (arr.length === k + 1) {
    let curNum = arr.join('');
    maxNum = maxNum < curNum ? curNum : maxNum;
    minNum = minNum > curNum ? curNum : minNum;

    return;
  }

  for (let i = 0; i < 10; i++) {
    const lastIdx = arr.length - 1;
    const sign = signs[lastIdx];
    if (!arr.includes(i)) {
      if (arr.length === 0 || eval(`${arr[lastIdx]}${sign}${i}`)) deflateSync([...arr, i]);
    }
  }
}

deflateSync([]);

console.log(maxNum);
console.log(minNum);
