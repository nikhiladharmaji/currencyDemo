import flask
from flask import request, jsonify, render_template
import CurrencyFormatter as cf

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/', methods=['GET'])
def home():
	return render_template("index.html")


@app.route('/api/v1/currency', methods=['GET'])
def api():
	if 'value' in request.args:
		value = request.args['value']
	if 'code' in request.args:
		code = request.args['code']
	if 'format' in request.args:
	    cformat = request.args['format']
	if 'culture' in request.args:
		culture = request.args['culture']
	if not 'culture' in request.args:
		culture = "en-gb"	

	else:
		return "Parameters Missing"

	return cf.currencyFormat(value,code,cformat,culture)

app.run()