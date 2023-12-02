const fs = require('fs');
const fileContent = fs.readFileSync('input.txt', 'utf-8');

const dataArray = fileContent.split('\n');


function replaceOccurrences(inputString) {
    const mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    };
    let d = 0;
    for (let a = 0; a < inputString.length; a++) {
        if (!isNaN(parseInt(inputString[a]))) {
            d *= 10;
            d += parseInt(inputString[a]);
        }
        for (let b in mapping) {
            if (inputString.substring(a, a + b.length) === b) {
                d *= 10;
                d += mapping[b];
                break;
            }
        }
    }

    return d;
}

const filteredArray = dataArray.map(replaceOccurrences);

console.log(filteredArray);

const sum = filteredArray.map((num) => {
    let numStr = num.toString();
    let fd = parseInt(numStr[0]);
    let sd = parseInt(numStr[numStr.length - 1]);
    return fd * 10 + sd;
});

let total = sum.reduce((a, b) => a + b, 0);


console.log(total);