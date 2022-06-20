let fedTax = document.currentScript.getAttribute("fedTax");
let stateTax = document.currentScript.getAttribute("stateTax");
let ficaTax = document.currentScript.getAttribute("ficaTax");
let totalTax = document.currentScript.getAttribute("totalTax");
let netPay = document.currentScript.getAttribute("netPay");
let salary = document.currentScript.getAttribute("salary");

let table = document.getElementById("breakdownTable");

let props = [
  { 1: salary, 2: "Yearly Income:" },
  { 1: fedTax, 2: "Federal Tax:" },
  { 1: stateTax, 2: "State Tax:" },
  { 1: ficaTax, 2: "FICA Tax:" },
  { 1: totalTax, 2: "Total Tax:" },
  { 1: netPay, 2: "Net Pay:" },
];

for (let i = 0; i < props.length; i++) {
  let row = table.insertRow(i + 1);
  let cell1 = row.insertCell(0);
  let cell2 = row.insertCell(1);
  cell1.innerHTML = props[i]["2"];
  cell2.innerHTML = props[i]["1"];
}
