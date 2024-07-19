let inputs = document.querySelectorAll(".input");
let btnSolve = document.querySelector(".btn-solve");
let maxLength = 1;

inputs.forEach((element) => {
  element.addEventListener("input", () => {
    if (element.value.length > maxLength) {
      element.value = element.value.slice(0, element.maxLength);
    }
  });
});

btnSolve.addEventListener("click", () => {
  let sudokuJSON = JSON.stringify(takeData(inputs));
  let url = `http://127.0.0.1:5000/${sudokuJSON}`;
  fetch(url);
});

function takeData(data) {
  let sudoku = [];
  let row = [];
  inputs.forEach((input, i) => {
    if ((i + 1) % 9 == 0) {
      row.push(Number(input.value));
      sudoku.push(row);
      row = [];
    } else {
      row.push(Number(input.value));
    }
  });
  return sudoku;
}
