from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

class PaymentForm(FlaskForm):
	date_recorded = DateField('Payment Date', default=datetime.now())
	payment_amount = IntegerField('Payment Amount', validators=[DataRequired()])
	submit = SubmitField('Submit Payment')

