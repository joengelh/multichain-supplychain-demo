from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import requests

views = Blueprint('views', __name__)

def getBalance(usr):
    address= 'http://' + usr.host + '/api/v1/balance'
    balance = requests.get(address, 
        json={'name': "USD"}).json()
    return float(balance["data"]["qty"])

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

@views.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    if request.method == 'POST':
        amount = request.form['amount']
        name = request.form['name']
        address = request.form['address']
        sendApi = 'http://' + current_user.host + '/api/v1/send'
        result = requests.post(sendApi, json={"name":name,
            "amount":float(amount),
            "address":address}).json()
        flash('Sending Successful!', category='success')
    api = 'http://' + current_user.host + '/api/v1/inventory'
    inventory = requests.get(api, json={}).json()
    return render_template("send.html", 
            user=current_user, 
            balance=getBalance(current_user),
            inventory=inventory["data"])

@views.route('/issue', methods=['GET', 'POST'])
@login_required
def issue():
    if request.method == 'POST':
        amount = request.form['amount']
        name = request.form['name']
        issueApi = 'http://' + current_user.host + '/api/v1/issue'
        result = requests.post(issueApi, json={"name":name,"amount":float(amount)}).json()
        try: 
            if result["message"] == "Internal Server Error":
                flash('No Permission to issue ' + name, category='error')
        except:
            flash('Issuing Successful!', category='success')
    api = 'http://' + current_user.host + '/api/v1/inventory'
    inventory = requests.get(api, json={}).json()
    return render_template("issue.html",
            user=current_user,
            balance=getBalance(current_user),
            inventory=inventory["data"])

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    api = 'http://' + current_user.host + '/api/v1/history'
    result = requests.get(api, json={}).json()
    return render_template("history.html",
            user=current_user,
            history=result["data"])

@views.route('/activate', methods=['GET', 'POST'])
@login_required
def activate():
    if request.method == 'POST':
        name = request.form['name']
        #take first 32 chars from name since more is not supported
        cutName = name[0:32]
        sendApi = 'http://' + current_user.host + '/api/v1/activate'
        result = requests.post(sendApi, json={"name":cutName}).json()
        flash('Activation Successful!', category='success')
    api = 'http://' + current_user.host + '/api/v1/listActive'
    active = requests.get(api, json={}).json()
    return render_template("activate.html", 
            user=current_user,
            active=active["data"])

@views.route('/deactivate', methods=['GET', 'POST'])
@login_required
def deactivate():
    if request.method == 'POST':
        name = request.form['name']
        sendApi = 'http://' + current_user.host + '/api/v1/deactivate'
        result = requests.post(sendApi, json={"name":name}).json()
        flash('Deactivation Successful!', category='success')
    api = 'http://' + current_user.host + '/api/v1/listActive'
    active = requests.get(api, json={}).json()
    return render_template("deactivate.html", 
            user=current_user,
            active=active["data"])

@views.route('/data', methods=['GET', 'POST'])
@login_required
def data():
    if request.method == 'POST':
        name = request.form['name']
        sendApi = 'http://' + current_user.host + '/api/v1/listItems'
        result = requests.get(sendApi, json={"name":name}).json()
        flash('Data Reading Successful!', category='success')
        return render_template("data.html", 
                user=current_user,
                items=result["data"])
    else:
        return render_template("data.html", user=current_user)

@views.route('/newExchange', methods=['GET', 'POST'])
@login_required
def newExchange():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        barter = request.form['barter']
        price = request.form['price']
        sendApi = 'http://' + current_user.host + '/api/v1/atomicExchange'
        result = requests.post(sendApi, json={"name":name,
            "amount":float(amount),"barter":barter,"price":float(price)}).json()
        flash('Atomic Exchange Created Successfuly!', category='success')
        return render_template("newExchange.html", 
            user=current_user,
            id=result["data"])
    else:
        return render_template("newExchange.html", 
            user=current_user)

@views.route('/manageExchange', methods=['GET', 'POST'])
@login_required
def manageExchange():
    if request.method == 'POST':
        proposal = request.form['id']
        if request.form.get('action') == 'accept':
            acceptApi = 'http://' + current_user.host + '/api/v1/acceptExchange'
            try:
                result = requests.post(acceptApi, json={"id":proposal}).json()
                flash('Atomic Exchange accepted Successfuly!', category='success')
            except: 
                flash('Atomic Exchange was not accepted!', category='error')
            return render_template("manageExchange.html", 
                user=current_user)
        elif request.form.get('action') == 'withdraw':
            withdrawApi = 'http://' + current_user.host + '/api/v1/withdrawExchange'
            try:
                result = requests.post(withdrawApi, json={"id":proposal}).json()
                flash('Atomic Exchange withdrawn Successfuly!', category='success')
            except: 
                flash('Atomic Exchange Withdrawal was not accepted!', category='error')
            return render_template("manageExchange.html", 
                user=current_user)
        elif request.form.get('action') == 'review':
            reviewApi = 'http://' + current_user.host + '/api/v1/reviewExchange'
            try:
                result = requests.get(reviewApi, json={"id":proposal}).json()
                review = result["data"]
            except: 
                flash('Atomic Exchange does not exist!', category='error')
            return render_template("manageExchange.html", 
                    user=current_user,
                    review=review)
    else:
        return render_template("manageExchange.html", 
            user=current_user)
