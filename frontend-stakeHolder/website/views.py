from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import requests
views = Blueprint('views', __name__)

def getBalance(usr):
    address= 'http://' + usr.host + '/api/v1/balance'
    balance = requests.get(address, 
        json={'asset': "USD"}).json()
    if balance["data"] is None:
        return 0
    else:
        return float(balance["data"])

def getWallet(usr):
    api = 'http://' + usr.host + '/api/v1/ownAddress'
    ownAddress = requests.get(api, json={}).json()
    return ownAddress["data"]

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", 
            user=current_user, 
            ownAddress=getWallet(current_user), 
            balance=getBalance(current_user))

#@views.route('/send', methods=['GET', 'POST'])
#@login_required
#def send():
    #if request.method == 'POST':
    #    amount = request.form['amount']
    #    name = request.form['name']
    #    address = request.form['address']
    #    api = 'http://' + usr.host + '/api/v1/send'
    #    result = request.post(api,
    #            json={'name':asset,'amount':amount,'address':address})

@views.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    if request.method == 'POST':
        amount = request.form['amount']
        requests.post('http://localhost:5001/api/v1/fund',
            json={'account': getWallet(current_user), 'amount': float(amount)})
        flash('Funding Successful!', category='success')
    else:
        api = 'http://' + current_user.host + '/api/v1/inventory'
        inventory = requests.get(api, json={}).json()
        print(inventory["data"])
    return render_template("send.html", 
            user=current_user, 
            balance=getBalance(current_user),
            inventory=inventory["data"])


@views.route('/fund', methods=['GET', 'POST'])
@login_required
def fund():
    if request.method == 'POST':
        amount = request.form['amount']
        requests.post('http://localhost:5001/api/v1/fund', 
            json={'account': getWallet(current_user), 'amount': float(amount)})
        flash('Funding Successful!', category='success')
    return render_template("fund.html", user=current_user, balance=getBalance(current_user))

# if the current logged in user is the bank, display the burn asset page
# else burn address on page
@views.route('/refund', methods=['GET', 'POST'])
@login_required
def refund():
    ownAddress = requests.get('http://localhost:5001/api/v1/ownAddress').json()
    if ownAddress["data"] == getWallet(current_user):    
        if request.method == 'POST':
            amount = request.form['amount']
            requests.post('http://localhost:5001/api/v1/refund', 
                json={'amount': float(amount)})
            flash('Refunding Successful!', category='success')
        return render_template("refund.html", user=current_user, balance=getBalance(current_user))
    else:
        burnAddress = requests.get('http://localhost:5001/api/v1/burnAddress').json()
        return render_template("burn.html", user=current_user, address=burnAddress['data'])
