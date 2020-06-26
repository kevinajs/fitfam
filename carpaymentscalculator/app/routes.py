from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Payment

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

@app.route('/viewpayments', methods=['GET','POST'])
def viewpayments():
	title = 'View a Payment'
	results = db.engine.execute('SELECT date_recorded, SUM(payment_amount) FROM Payment GROUP BY date_recorded').fetchall()
	print(type(results))
	print(results)
	for row in results:
		for x in row:
			print(x)

	for row in results:
		for x in row:
			print(x)


	returned = [row[0] for row in results]

	return render_template('viewpayments.html',
	                       title=title,
	                       id = returned
	                       )

