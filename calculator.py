salary = float(input("How much do you earn per year? "));
gross_income = salary - 12550;
tax = 0.0;
tax_rate = {
    "1": {
        "rate": 0.1,
        "threshold": 9950,
    },
    "2": {
        "rate": 0.12,
        "threshold": 40525
    },
    "3": {
        "rate": 0.22,
        "threshold": 86375
    },
    "4": {
        "rate": 0.24,
        "threshold": 164925
    },
    "5": {
        "rate": 0.32,
        "threshold": 209425
    },
    "6": {
        "rate": 0.35,
        "threshold": 523600
    },
    "7": {
        "rate": 0.37
    }
}
br1 = tax_rate["1"]["threshold"] * tax_rate["1"]["rate"];
br2 = (tax_rate["2"]["threshold"] - tax_rate["1"]["threshold"]) * tax_rate["2"]["rate"];
br3 = (tax_rate["3"]["threshold"] - tax_rate["2"]["threshold"]) * tax_rate["3"]["rate"];
br4 = (tax_rate["4"]["threshold"] - tax_rate["3"]["threshold"]) * tax_rate["4"]["rate"];
br5 = (tax_rate["5"]["threshold"] - tax_rate["4"]["threshold"]) * tax_rate["5"]["rate"];
br6 = (tax_rate["6"]["threshold"] - tax_rate["5"]["threshold"]) * tax_rate["6"]["rate"];

def calc_tax(income):
    if income <= 0:
        tax = 0.0;
        taxable: 0.0;
    elif income < tax_rate["1"]["threshold"]:
        tax = income * tax_rate["1"]["rate"];
        taxable = income;
    elif income > tax_rate["1"]["threshold"] and income <= tax_rate["2"]["threshold"]:
        taxable = (income - tax_rate["1"]["threshold"]) * tax_rate["2"]["rate"];
        tax = br1 + taxable;
    elif income > tax_rate["2"]["threshold"] and income <= tax_rate["3"]["threshold"]:
        taxable = (income - tax_rate["2"]["threshold"]) * tax_rate["3"]["rate"];
        tax = br1 + br2 + taxable;
    elif income > tax_rate["3"]["threshold"] and income <= tax_rate["4"]["threshold"]:
        taxable = (income - tax_rate["3"]["threshold"]) * tax_rate["4"]["rate"];
        tax = br1 + br2 + br3 + taxable;
    elif income > tax_rate["4"]["threshold"] and income <= tax_rate["5"]["threshold"]:
        taxable = (income - tax_rate["4"]["threshold"]) * tax_rate["5"]["rate"];
        tax = br1 + br2 + br3 + br4 + taxable;
    elif income > tax_rate["5"]["threshold"] and income <= tax_rate["6"]["threshold"]:
        taxable = (income - tax_rate["5"]["threshold"]) * tax_rate["6"]["rate"];
        tax = br1 + br2 + br3 + br4 + br5 + taxable;
    elif income > tax_rate["6"]["threshold"]:
        taxable = (income - tax_rate["6"]["threshold"]) * tax_rate["7"]["rate"];
        tax = br1 + br2 + br3 + br4 + br5 + br6 + taxable;
    print("Your federal tax is: " + str(tax));

calc_tax(gross_income);



