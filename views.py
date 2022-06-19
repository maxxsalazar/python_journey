from flask import Blueprint, render_template, request
from calculator import *

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    return render_template('index.html', title='Income Tax Calculator')

@views.route('/calculator')
def calculator():
    args = request.args
    salary = args.get('income')
    fedTax = calc_fed_tax(int(salary))
    stateTax = calc_state_tax(int(salary))
    ficaTax = calc_fica_tax(int(salary))
    totalTax = fedTax + stateTax + ficaTax;
    netPay = int(salary) - totalTax;
    return render_template('calculator.html', title='Income Tax Calculator', fedTax=fedTax, stateTax=stateTax, ficaTax=ficaTax,totalTax=totalTax, netPay=netPay)