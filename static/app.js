let fedTax = document.currentScript.getAttribute("fedTax"); //1
let stateTax = document.currentScript.getAttribute("stateTax"); //2
let ficaTax = document.currentScript.getAttribute("ficaTax"); //3
let totalTax = document.currentScript.getAttribute("totalTax"); //4
let netPay = document.currentScript.getAttribute("netPay"); //5

let table = document.getElementById("breakdownTable");

let props = [
  { 1: fedTax, 2: "Federal Tax:" },
  { 1: stateTax, 2: "State Tax:" },
  { 1: ficaTax, 2: "FICA Tax:" },
  { 1: totalTax, 2: "Total Tax:" },
  { 1: netPay, 2: "Net Pay:" },
];

// fill table with data
for (let i = 0; i < props.length; i++) {
  let row = table.insertRow(i + 1);
  let cell1 = row.insertCell(0);
  let cell2 = row.insertCell(1);
  cell1.innerHTML = props[i]["2"];
  cell2.innerHTML = props[i]["1"];
}
