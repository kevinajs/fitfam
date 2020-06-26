from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class PaymentForm(FlaskForm):
	payment_amount = IntegerField('Payment Amount', validators=[DataRequired()])
	submit = SubmitField('Submit Payment')

