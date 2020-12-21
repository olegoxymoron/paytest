from hashlib import sha256
from collections import OrderedDict
import requests
from flask import render_template

currencies = {
    'USD': '840',
    'EUR': '978',
    'RUB': '643'
}

parameters = {
    'shop_id': '5',
    'secretKey': 'SecretKey01',
    'payway': 'payeer_rub',
    'shop_order_id': '4126'
}

def invoice(params):
    url = 'https://core.piastrix.com/invoice/create'
    headers = {'content-type': 'application/json'}

    params['payway'] = parameters['payway']
    params['currency'] = currencies[params['currency']]
    params['shop_id'] = parameters['shop_id']
    params['shop_order_id'] = parameters['shop_order_id']

    required_params = params.copy()
    del required_params['description']
    
    required_params = OrderedDict(sorted(required_params.items()))
    sign_str = ':'.join(required_params.values()) + parameters['secretKey']
    params['sign'] = sha256(str.encode(sign_str)).hexdigest()

    response = requests.post(url, json=params, headers=headers)

    print(response.content.decode('utf-8'))


def bill(params):
    url = 'https://core.piastrix.com/bill/create'
    headers = {'content-type': 'application/json'}

    params['currency'] = currencies[params['currency']]
    params['payer_currency'] = params['currency']
    del params['currency']
    params['shop_amount'] = params['amount']
    del params['amount']

    params['shop_id'] = parameters['shop_id']
    params['shop_order_id'] = parameters['shop_order_id']
    params['shop_currency'] = '840'

    required_params = params.copy()
    del required_params['description']
    
    required_params = OrderedDict(sorted(required_params.items()))
    sign_str = ':'.join(required_params.values()) + parameters['secretKey']
    params['sign'] = sha256(str.encode(sign_str)).hexdigest()

    response = requests.post(url, json=params, headers=headers)

    return response

def pay(params):
    url = 'https://pay.piastrix.com/ru/pay'
    headers = {'content-type': 'application/json'}

    params['currency'] = currencies[params['currency']]
    params['shop_id'] = parameters['shop_id']
    params['shop_order_id'] = parameters['shop_order_id']

    required_params = params.copy()
    del required_params['description']
    
    print(required_params)
    required_params = OrderedDict(sorted(required_params.items()))
    sign_str = ':'.join(required_params.values()) + parameters['secretKey']
    params['sign'] = sha256(str.encode(sign_str)).hexdigest()

    print(sign_str)

    return render_template('pay_form.html', data=params)