from flask import Flask, request, render_template, redirect
from pay_methods import methods as m

import logging
from flask.logging import default_handler

app = Flask(__name__)

root = logging.getLogger()
root.addHandler(default_handler)

@app.route('/', methods=['GET'])
def start_page():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    amount = request.form.get('amount')
    currency = request.form.get('currency')
    description = request.form.get('description')

    params = {
        'amount': amount,
        'currency': currency,
        'description': description
    }

    if currency == 'RUB':
        resp_ = m.invoice(params)
    elif currency == 'EUR':
        resp = m.pay(params)
    elif currency == 'USD':
        resp_ = m.bill(params).json()

        if resp_['error_code'] == 0:
            url = resp_['data']['url']
            resp = redirect(url, code=302)
        else:
            resp = resp_['message']

    return resp