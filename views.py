from flask import Blueprint, render_template, request, redirect, url_for
from calculator import *

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    return render_template('index.html', title='Income Tax Calculator')

@views.route('/calculator')
def calculator():
    args = request.args
    salary = args.get('income')
    if salary == None or salary == '':
        return redirect(url_for('views.index'))
    else:
        fedTax = calc_fed_tax(float(salary))
        stateTax = calc_state_tax(float(salary))
        ficaTax = calc_fica_tax(float(salary))
        totalTax = fedTax + stateTax + ficaTax;
        netPay = float(salary) - totalTax;
        return render_template('calculator.html', title='Income Tax Calculator', fedTax=fedTax, stateTax=stateTax, ficaTax=ficaTax,totalTax=totalTax, netPay=netPay, salary=float(salary))
