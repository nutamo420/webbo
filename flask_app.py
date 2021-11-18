from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/stock')
def entername():
    return render_template('form.html')

@app.route('/result', methods = ['GET'])
def price_result():
    # result = requests.get("http://data.fixer.io/api/latest?access_key=WPA26IESV0A5ACK1")
    # jsondata = result.json()
    # eur_thb = jsondata['rates']['THB']
    # eur = request.args.get('amount')
    # thb = float(eur)*float(eur_thb)
    # return render_template('result.html',amount_eur=eur,amount_thb=thb)
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=WPA26IESV0A5ACK1'
    r = requests.get(url)
    data = r.json()

    print(data)