from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
	title = 'Home'

	return render_template('index.html',
	                       title=title)

@app.route('/balance')
def balance():
	title = 'View Payments'

	return render_template('balance.html',
	                       title=title)

@app.route('/payments')
def payment():
	title = 'Make a Payment'

	return render_template('payments.html',
	                       title=title)

@app.route('/viewpayments')
def viewpayments():
	title = 'View a Payment'

	return render_template('viewpayments.html',
	                       title=title)

