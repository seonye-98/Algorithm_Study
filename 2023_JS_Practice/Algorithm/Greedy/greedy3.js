//https://www.acmicpc.net/problem/13305
const path = require('path');
const fs = require('fs');
const input = fs
  .readFileSync(path.join(__dirname, 'dev', 'stdin'))
  .toString()
  .trim()
  .split('\n');