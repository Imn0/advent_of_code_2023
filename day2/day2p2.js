"use strict";
exports.__esModule = true;
var fs = require("fs");
function mapRGB(data) {
    var r_max = 0;
    var g_max = 0;
    var b_max = 0;
    var games = data[1];
    for (var game in games) {
        for (var i = 0; i < games[game].length; i++) {
            var val = parseInt(games[game][i].trim().split(" ")[0]);
            if (games[game][i].includes("red")) {
                if (val > r_max) {
                    r_max = val;
                }
            }
            else if (games[game][i].includes("green")) {
                if (val > g_max) {
                    g_max = val;
                }
            }
            else if (games[game][i].includes("blue")) {
                if (val > b_max) {
                    b_max = val;
                }
            }
        }
    }
    return g_max * r_max * b_max;
}
var red_total = 12;
var green_total = 13;
var blue_total = 14;
var fileContent = fs.readFileSync("input.txt", "utf-8");
var dataArray = fileContent.split("\n");
var gameParsed = dataArray.map(function (row) { return row.split(":"); });
var dataParsed = gameParsed
    .map(function (data) {
    return data.flatMap(function (item) { return item.split(";").map(function (subItem) { return subItem.trim(); }); });
})
    .map(function (data) { return data.map(function (item) { return item.split(","); }); })
    .map(function (data) { return [data[0], data.slice(1)]; })
    .map(function (data) { return mapRGB(data); })
    .reduce(function (partialSum, a) { return partialSum + a; }, 0);
var answer = dataParsed;
console.log(answer);
