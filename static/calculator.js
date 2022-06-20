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
const states = {
  AL: "Alabama",
  AK: "Alaska",
  AZ: "Arizona",
  AR: "Arkansas",
  CA: "California",
  CO: "Colorado",
  CT: "Connecticut",
  DE: "Delaware",
  DC: "District Of Columbia",
  FL: "Florida",
  GA: "Georgia",
  HI: "Hawaii",
  ID: "Idaho",
  IL: "Illinois",
  IN: "Indiana",
  IA: "Iowa",
  KS: "Kansas",
  KY: "Kentucky",
  LA: "Louisiana",
  ME: "Maine",
  MD: "Maryland",
  MA: "Massachusetts",
  MI: "Michigan",
  MN: "Minnesota",
  MS: "Mississippi",
  MO: "Missouri",
  MT: "Montana",
  NE: "Nebraska",
  NV: "Nevada",
  NH: "New Hampshire",
  NJ: "New Jersey",
  NM: "New Mexico",
  NY: "New York",
  NC: "North Carolina",
  ND: "North Dakota",
  OH: "Ohio",
  OK: "Oklahoma",
  OR: "Oregon",
  PA: "Pennsylvania",
  RI: "Rhode Island",
  SC: "South Carolina",
  SD: "South Dakota",
  TN: "Tennessee",
  TX: "Texas",
  UT: "Utah",
  VT: "Vermont",
  VA: "Virginia",
  WA: "Washington",
  WV: "West Virginia",
  WI: "Wisconsin",
  WY: "Wyoming",
};
let dropdown = document.getElementById("selectState");
// console log each state
for (let key in states) {
  let option = document.createElement("option");
  option.value = key;
  option.className = "form-control";
  option.innerText = states[key];
  dropdown.appendChild(option);
}
