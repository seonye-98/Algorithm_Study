//이진탐색 문제풀이1

//파라메트릭 서치 문제 풀이
//https://www.acmicpc.net/problem/2512
//난이도 : 실버2

/*
정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
2. 모든 요청이 배정될 수 없는 경우 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는
모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서 요청한 금액을 그대로 배정

변화되는 값 x는 상한액
상한액은 N부터 1,000,000,000 이하
f(x)는 단조 감소 함수

상한액을 1부터 예산요청 배열의 최대값까지 이진탐색을 통해 최적의 해를 찾는다.
*/

const path = require('path');
const fs = require('fs');
const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

const N = Number(input[0]);
const arr = input[1].split(' ').map(Number);
const m = Number(input[2]);

let start = 1;
let end = arr.reduce((a, b) => Math.max(a, b));

let result = 0;

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0; //배정된 예산의 총액
  for (x of arr) {
    total += Math.min(mid, x);
  }
  if (total <= m) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);

//https://www.acmicpc.net/problem/2805
// 난이도 : 실버2
//이진탐색, 파라메트릭 서치

/*
절단기에 높이 H 지정, 한줄에 연속해 있는 나무 모두 절단
높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고 낮은 나무는 잘리지 않는다.
적어도 M미터의 나무를 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

N : 나무의 수, M : 가져가려고 하는 나무의 길이
나무의 높이, 나무의 높이의 합은 항상 M보다 크거나 같다

절단기의 높이 H를 변수로 지정하면 될 것 같다.
H가 증가하는 경우 얻을 수 있는 나무의 양이 감소하고,
H가 감소하는 경우 얻을 수 있는 나무의 양이 증가한다.
*/

const path = require('path');
const fs = require('fs');
// const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

// const [N, M] = input[0].split(' ').map(Number);
// const trees = input[1].split(' ').map(Number);

// let start = 0;
// let end = trees.reduce((a, b) => Math.max(a, b));

// let answer;
while (start <= end) {
  let result = 0;
  let mid = parseInt((start + end) / 2);

  for (t of trees) {
    result += Math.max(t - mid, 0);
  }
  if (result >= M) {
    answer = mid;
    start = mid + 1;
  } else if (result < M) {
    end = mid - 1;
  }
}

console.log(answer);

//https://www.acmicpc.net/problem/1654
// 난이도 : 실버2
//이진탐색, 파라메트릭 서치

/*
박성원은 N개의 랜선을 만들어야하고
오영식은 자체적으로 K개의 랜선을 가지고있지만, 길이가 제각각
박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶어
K개의 랜선을 잘라서 만들어야 함

300cm짜리 랜선을 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함, 최대 랜선의 길이를 구하는 프로그램 작성

K : 오영식이 이미 가지고 있는 랜선의 개수, N : 필요한 랜선의 개수
K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 입력

N개를 만들 수 있는 랜선의 최대길이를 변수로 잡자
변수가 커지면 만들 수 있는 랜선의 길이는 작아지고, 작아지면 많아진다.
*/

const path = require('path');
const fs = require('fs');
// const input = fs.readFileSync(path.join(__dirname, 'dev', 'stdin')).toString().trim().split('\n');

// const [K, N] = input[0].split(' ').map(Number);
// const lines = input.splice(1, K).map((line) => Number(line.trim()));

// let start = 1;
// let end = lines.reduce((a, b) => Math.max(a, b));

let answer;

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0;
  for (l of lines) {
    total += parseInt(l / mid);
  }

  if (total < N) {
    end = mid - 1;
  } else {
    answer = mid;
    start = mid + 1;
  }
}

console.log(answer);
