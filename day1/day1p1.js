const fs = require('fs');
const fileContent = fs.readFileSync('input.txt', 'utf-8');

const dataArray = fileContent.split('\n');

const filteredArray = dataArray.map((str) => str.replace(/[a-zA-Z]/g, ''));

const sum = filteredArray.map((num) => {
    let numStr = num.toString();
    let fd = parseInt(numStr[0]);
    let sd = parseInt(numStr[numStr.length - 1]);
    return fd * 10 + sd;
});

let total = sum.reduce((a, b) => a + b, 0);

console.log(total);