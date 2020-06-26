from app import db
from datetime import datetime

class Payment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_recorded = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	payment_amount = db.Column(db.Integer)
	payment_type = db.Column(db.String(9), default='Automatic')

	def __repr__(self):
		return '<Payment Amount {}>'.format(self.payment_amount)
