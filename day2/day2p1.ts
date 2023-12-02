import * as fs from "fs";

function mapRGB(data: (string[] | string[][])[]) {
  const games = data[1];
  for (let game in games) {
    for (let i = 0; i < games[game].length; i++) {
      const val = parseInt(games[game][i].trim().split(" ")[0]);
      if (games[game][i].includes("red")) {
        if (val > red_total) {
          return 0;
        }
      } else if (games[game][i].includes("green")) {
        if (val > green_total) {
          return 0;
        }
      } else if (games[game][i].includes("blue")) {
        if (val > blue_total) {
          return 0;
        }
      }
    }
  }

  return parseInt(String(data[0][0]).split(" ")[1]);
}

const red_total = 12;
const green_total = 13;
const blue_total = 14;

const fileContent = fs.readFileSync("input.txt", "utf-8");
const dataArray = fileContent.split("\n");
const gameParsed = dataArray.map((row: String) => row.split(":"));
const dataParsed = gameParsed
  .map((data) =>
    data.flatMap((item) => item.split(";").map((subItem) => subItem.trim()))
  )
  .map((data) => data.map((item) => item.split(",")))
  .map((data) => [data[0], data.slice(1)])
  .map((data) => mapRGB(data))
  .reduce((partialSum, a) => partialSum + a, 0);

const answer = dataParsed;
console.log(answer);
