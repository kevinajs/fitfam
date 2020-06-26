from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import PaymentForm
from app.models import Payment

@app.route('/')
@app.route('/index')
def index():
	title = 'Home'

	return render_template('index.html',
	                       title=title)

@app.route('/balance')
def balance():
	title = 'Check Balance'
	TOTAL_AMOUNT = 8631.48
	query = db.engine.execute("""
	                                SELECT SUM(payment_amount)
	                                FROM Payment
	                                """
	                                ).fetchone()
	amount_paid = query[0]
	to_be_paid = TOTAL_AMOUNT - query[0]

	return render_template('balance.html',
	                       title=title,
	                       total_amount='${:,.2f}'.format(TOTAL_AMOUNT),
	                       amount_paid='${:,.2f}'.format(amount_paid),
	                       to_be_paid='${:,.2f}'.format(to_be_paid))

@app.route('/payments', methods=['GET','POST'])
def payment():
	title = 'Make a Payment'
	form = PaymentForm()
	if form.validate_on_submit():
		payment = Payment(payment_amount=form.payment_amount.data)
		print(payment)
		db.session.add(payment)
		db.session.commit()
		flash('Payment Successful!')
		return redirect('payments')
	return render_template('payments.html',
	                       title=title,
	                       form=form)

@app.route('/viewpayments', methods=['GET','POST'])
def viewpayments():
	title = 'View a Payment'
	query = db.engine.execute("""
	                            SELECT	DATE(date_recorded) AS date_recorded
	                            		,SUM(payment_amount) AS payment_amount
	                            FROM Payment
	                            GROUP BY DATE(date_recorded)
	                            """)

	results = query.fetchall()

	column_names = [col for col in query.keys()]

	return render_template('viewpayments.html',
	                       title=title,
	                       column_names=column_names,
	                       results=results
	                       )

