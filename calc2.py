fed_tax_rate = {
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
state_tax_rate = {
    "CA": {
        "1": {
            "rate": 0.01,
            "threshold": 9325,
        },
        "2": {
            "rate": 0.02,
            "threshold": 22107,
        },
        "3": {
            "rate": 0.04,
            "threshold": 34892,
        },
        "4":{
            "rate": 0.06,
            "threshold": 48435,
        },
        "5":{
            "rate": 0.08,
            "threshold": 61214,
        },
        "6":{
            "rate": 0.093,
            "threshold": 312686,
        },
        "7":{
            "rate": 0.103,
            "threshold": 375221,
        },
        "8":{
            "rate": 0.113,
            "threshold": 625369,
        },
        "9":{
            "rate": 0.123,
            "threshold": 1000000,
        },
        "10":{
            "rate": 0.133,
        }
    }
}
fbr1 = fed_tax_rate["1"]["threshold"] * fed_tax_rate["1"]["rate"];
fbr2 = (fed_tax_rate["2"]["threshold"] - fed_tax_rate["1"]["threshold"]) * fed_tax_rate["2"]["rate"];
fbr3 = (fed_tax_rate["3"]["threshold"] - fed_tax_rate["2"]["threshold"]) * fed_tax_rate["3"]["rate"];
fbr4 = (fed_tax_rate["4"]["threshold"] - fed_tax_rate["3"]["threshold"]) * fed_tax_rate["4"]["rate"];
fbr5 = (fed_tax_rate["5"]["threshold"] - fed_tax_rate["4"]["threshold"]) * fed_tax_rate["5"]["rate"];
fbr6 = (fed_tax_rate["6"]["threshold"] - fed_tax_rate["5"]["threshold"]) * fed_tax_rate["6"]["rate"];

def calc_fed_tax(income):
    income -= 12550;

    if income <= 0:
        tax = 0.0;
        taxable: 0.0;
    elif income < fed_tax_rate["1"]["threshold"]:
        tax = income * fed_tax_rate["1"]["rate"];
        taxable = income;
    elif income > fed_tax_rate["1"]["threshold"] and income <= fed_tax_rate["2"]["threshold"]:
        taxable = (income - fed_tax_rate["1"]["threshold"]) * fed_tax_rate["2"]["rate"];
        tax = fbr1 + taxable;
    elif income > fed_tax_rate["2"]["threshold"] and income <= fed_tax_rate["3"]["threshold"]:
        taxable = (income - fed_tax_rate["2"]["threshold"]) * fed_tax_rate["3"]["rate"];
        tax = fbr1 + fbr2 + taxable;
    elif income > fed_tax_rate["3"]["threshold"] and income <= fed_tax_rate["4"]["threshold"]:
        taxable = (income - fed_tax_rate["3"]["threshold"]) * fed_tax_rate["4"]["rate"];
        tax = fbr1 + fbr2 + fbr3 + taxable;
    elif income > fed_tax_rate["4"]["threshold"] and income <= fed_tax_rate["5"]["threshold"]:
        taxable = (income - fed_tax_rate["4"]["threshold"]) * fed_tax_rate["5"]["rate"];
        tax = fbr1 + fbr2 + fbr3 + fbr4 + taxable;
    elif income > fed_tax_rate["5"]["threshold"] and income <= fed_tax_rate["6"]["threshold"]:
        taxable = (income - fed_tax_rate["5"]["threshold"]) * fed_tax_rate["6"]["rate"];
        tax = fbr1 + fbr2 + fbr3 + fbr4 + fbr5 + taxable;
    elif income > fed_tax_rate["6"]["threshold"]:
        taxable = (income - fed_tax_rate["6"]["threshold"]) * fed_tax_rate["7"]["rate"];
        tax = fbr1 + fbr2 + fbr3 + fbr4 + fbr5 + fbr6 + taxable;
    return tax;


sbr1 = state_tax_rate["CA"]["1"]["threshold"] * state_tax_rate["CA"]["1"]["rate"];
sbr2 = (state_tax_rate["CA"]["2"]["threshold"] - state_tax_rate["CA"]["1"]["threshold"]) * state_tax_rate["CA"]["2"]["rate"];
sbr3 = (state_tax_rate["CA"]["3"]["threshold"] - state_tax_rate["CA"]["2"]["threshold"]) * state_tax_rate["CA"]["3"]["rate"];
sbr4 = (state_tax_rate["CA"]["4"]["threshold"] - state_tax_rate["CA"]["3"]["threshold"]) * state_tax_rate["CA"]["4"]["rate"];
sbr5 = (state_tax_rate["CA"]["5"]["threshold"] - state_tax_rate["CA"]["4"]["threshold"]) * state_tax_rate["CA"]["5"]["rate"];
sbr6 = (state_tax_rate["CA"]["6"]["threshold"] - state_tax_rate["CA"]["5"]["threshold"]) * state_tax_rate["CA"]["6"]["rate"];
sbr7 = (state_tax_rate["CA"]["7"]["threshold"] - state_tax_rate["CA"]["6"]["threshold"]) * state_tax_rate["CA"]["7"]["rate"];
sbr8 = (state_tax_rate["CA"]["8"]["threshold"] - state_tax_rate["CA"]["7"]["threshold"]) * state_tax_rate["CA"]["8"]["rate"];
sbr9 = (state_tax_rate["CA"]["9"]["threshold"] - state_tax_rate["CA"]["8"]["threshold"]) * state_tax_rate["CA"]["9"]["rate"];

def calc_state_tax(income):
    income -= 4803;
    if income <= 0:
        tax = 0.0;
        taxable: 0.0;
    elif income < state_tax_rate["CA"]["1"]["threshold"]:
        tax = income * state_tax_rate["CA"]["1"]["rate"];
        taxable = income;
    elif income > state_tax_rate["CA"]["1"]["threshold"] and income <= state_tax_rate["CA"]["2"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["1"]["threshold"]) * state_tax_rate["CA"]["2"]["rate"];
        tax = sbr1 + taxable;
    elif income > state_tax_rate["CA"]["2"]["threshold"] and income <= state_tax_rate["CA"]["3"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["2"]["threshold"]) * state_tax_rate["CA"]["3"]["rate"];
        tax = sbr1 + sbr2 + taxable;
    elif income > state_tax_rate["CA"]["3"]["threshold"] and income <= state_tax_rate["CA"]["4"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["3"]["threshold"]) * state_tax_rate["CA"]["4"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + taxable;
    elif income > state_tax_rate["CA"]["4"]["threshold"] and income <= state_tax_rate["CA"]["5"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["4"]["threshold"]) * state_tax_rate["CA"]["5"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + taxable;
    elif income > state_tax_rate["CA"]["5"]["threshold"] and income <= state_tax_rate["CA"]["6"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["5"]["threshold"]) * state_tax_rate["CA"]["6"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + sbr5 + taxable;
    elif income > state_tax_rate["CA"]["6"]["threshold"] and income <= state_tax_rate["CA"]["7"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["6"]["threshold"]) * state_tax_rate["CA"]["7"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + sbr5 + sbr6 + taxable;
    elif income > state_tax_rate["CA"]["7"]["threshold"] and income <= state_tax_rate["CA"]["8"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["7"]["threshold"]) * state_tax_rate["CA"]["8"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + sbr5 + sbr6 + sbr7 + taxable;
    elif income > state_tax_rate["CA"]["8"]["threshold"] and income <= state_tax_rate["CA"]["9"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["8"]["threshold"]) * state_tax_rate["CA"]["9"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + sbr5 + sbr6 + sbr7 + sbr8 + taxable;
    elif income > state_tax_rate["CA"]["9"]["threshold"]:
        taxable = (income - state_tax_rate["CA"]["9"]["threshold"]) * state_tax_rate["CA"]["10"]["rate"];
        tax = sbr1 + sbr2 + sbr3 + sbr4 + sbr5 + sbr6 + sbr7 + sbr8 + sbr9 + taxable;
    return tax;

def calc_fica_tax(income):
    fica = 0.0;

    if income <= 147000:
        fica = income * 0.0765;
    elif income > 147000 and income <= 200000:
        sst = 147000 * 0.062;
        medicare = income * 0.0145;
        fica = sst + medicare;
    else:
        sst = 147000 * 0.062;
        medicare1 = 200000 * 0.0145;
        medicare2 = (income - 200000) * 0.0235;
        fica = sst + medicare1 + medicare2;
    return fica;

# total_fed_tax = calc_fed_tax(350000);
# total_state_tax = calc_state_tax(350000);
# total_fica = calc_fica_tax(350000);
# total_tax = total_fed_tax + total_state_tax + total_fica;
# take_home_pay = 350000 - total_tax;

# print("\n- Federal income tax: ${:,.2f}".format(total_fed_tax) + "\n- State income tax: ${:,.2f}".format(total_state_tax) + "\n- FICA tax: ${:,.2f}".format(total_fica));
# print("- Total income tax: ${:,.2f}".format(total_tax));
# print("- Total take-home pay: ${:,.2f}".format(take_home_pay));
# print("\n");
# print("**This is an educational project and does not constitue financial advice.**\n");