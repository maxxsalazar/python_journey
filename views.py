from flask import Blueprint, render_template, request
from calc2 import *

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    return render_template('index.html', title='Home Page')

@views.route('/calculator')
def calculator():
    args = request.args
    salary = args.get('income')
    fedTax = calc_fed_tax(int(salary))
    stateTax = calc_state_tax(int(salary))
    ficaTax = calc_fica_tax(int(salary))
    totalTax = fedTax + stateTax + ficaTax;
    takeHome = int(salary) - totalTax;
    return render_template('index.html', title='Tax Calculator', fedTax=fedTax, stateTax=stateTax, ficaTax=ficaTax,totalTax=totalTax, takeHome=takeHome)