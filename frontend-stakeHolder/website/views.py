from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import requests
import ast
import os
from dotenv import load_dotenv

views = Blueprint('views', __name__)

def getNodeAddress():
    load_dotenv()
    nodes = ast.literal_eval(os.getenv('NODES'))
    currentNode = next((node for node in nodes if node['name'] == current_user.name), None)
    apiAddress = 'http://localhost:' + str(currentNode['port']) + '/api/v1'
    return apiAddress

def getBalance(usr):
    balance = requests.get('http://localhost:5001/api/v1/balance', 
        json={'account': usr.wallet}).json()
    if balance["data"] is None:
        return 0
    else:
        return float(balance["data"]["qty"])

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user, balance=getBalance(current_user))

@views.route('/fund', methods=['GET', 'POST'])
@login_required
def fund():
    if request.method == 'POST':
        amount = request.form['amount']
        requests.post('http://localhost:5001/api/v1/fund', 
            json={'account': current_user.wallet, 'amount': float(amount)})
        flash('Funding Successful!', category='success')
    return render_template("fund.html", user=current_user, balance=getBalance(current_user))

# if the current logged in user is the bank, display the burn asset page
# else burn address on page
@views.route('/refund', methods=['GET', 'POST'])
@login_required
def refund():
    ownAddress = requests.get('http://localhost:5001/api/v1/ownAddress').json()
    if ownAddress["data"] == current_user.wallet:    
        if request.method == 'POST':
            amount = request.form['amount']
            requests.post('http://localhost:5001/api/v1/refund', 
                json={'amount': float(amount)})
            flash('Refunding Successful!', category='success')
        return render_template("refund.html", user=current_user, balance=getBalance(current_user))
    else:
        burnAddress = requests.get('http://localhost:5001/api/v1/burnAddress').json()
        return render_template("burn.html", user=current_user, address=burnAddress['data'])
