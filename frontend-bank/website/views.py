from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import requests

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    #get current balance by calling the blockchain api
    balance = requests.post('http://localhost:5001/api/v1/balance', 
        json={'account': '17PBfmGiEUt8diTd3fD8idpnFPXiiiX4FacfzL'}).json()
    return render_template("home.html", user=current_user, balance=balance["data"]["qty"])

@views.route('/fund', methods=['GET', 'POST'])
@login_required
def fund():
    if request.method == 'POST':
        amount = request.form['amount']
        print(amount)
        print(type(amount))
        requests.post('http://localhost:5001/api/v1/fund', 
            json={'account': current_user.wallet, 'amount': float(amount)})
        flash('Funding Successful!', category='success')
    #get current balance by calling the blockchain
    balance = requests.post('http://localhost:5001/api/v1/balance', 
        json={'account': current_user.wallet}).json()
    return render_template("fund.html", user=current_user, balance=balance["data"]["qty"])

@views.route('/refund', methods=['GET', 'POST'])
@login_required
def refund():
    if request.method == 'POST':
        amount = request.form['amount']
        print(amount)
        print(type(amount))
        requests.post('http://localhost:5001/api/v1/refund', 
            json={'amount': float(amount)})
        flash('Refunding Successful!', category='success')
    #get current balance by calling the blockchain
    balance = requests.post('http://localhost:5001/api/v1/balance', 
        json={'account': current_user.wallet}).json()
    return render_template("refund.html", user=current_user, balance=balance["data"]["qty"])

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
