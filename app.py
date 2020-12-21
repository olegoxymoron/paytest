from flask import Flask, request, render_template
from pay_methods import methods as m

app = Flask(__name__)

method = {
    'RUB': m.invoice,
    'EUR': m.pay,
    'USD': m.bill
}

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

    return method[currency](params)