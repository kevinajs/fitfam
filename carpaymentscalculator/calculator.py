from datetime import datetime, timedelta
from flask import flask
import psycopg2

# Financed Amount 7553.92
# Interest Rate: 8.99%
# Payment: 110.66
# of Payments: 78
# Starts on June 19.

TOTAL_AMOUNT = 8631.48
INTEREST_RATE = .0899
BIWEEKLY_PAYMENT = 110.66
NUMBER_OF_PAYMENTS = 78
NUMBER_OF_DAYS_TOTAL = NUMBER_OF_PAYMENTS * 14

#Classes.

# class Database(object):
# 	def __init__(self):
# 		self.connection = psycopg2.connect(
# 		                              host='localhost',
# 		                              database='payment_tracker',
# 		                              user='postgres',
# 		                              password='admin')
# 		self.connection.set_session(autocommit=True)

# 	def close_connection():
# 		self.connection.close()

#Functions.

def makePayment(amount=BIWEEKLY_PAYMENT, payment_type='Regular'):

	connection = psycopg2.connect(
	                              host='localhost',
	                              database='payment_tracker',
	                              user='postgres',
	                              password='admin')

	record_tuple = (datetime.now(),
					amount,
	             	'Lump Sum')

	with connection.cursor() as cursor:
		cursor.execute(""" INSERT INTO payments(date_recorded,
		               							payment_amount,
		               							payment_type)

		               		VALUES (%s -- date_recorded
		               				,%s -- payment_amount
		               				,%s) -- payment_type
		               	""", record_tuple)
		connection.commit()
		connection.close()

def remainingBalance():

	connection = psycopg2.connect(
	                              host='localhost',
	                              database='payment_tracker',
	                              user='postgres',
	                              password='admin')

	with connection.cursor() as cursor:
		cursor.execute(""" SELECT SUM(payment_amount)
		               		FROM payments
		               """)

		results = cursor.fetchone()
		connection.close()

		return results

def viewPaymentsMade():
	connection = psycopg2.connect(
	                              host='localhost',
	                              database='payment_tracker',
	                              user='postgres',
	                              password='admin')

	with connection.cursor() as cursor:
		cursor.execute(""" SELECT date_recorded AS "Date Recorded"
								  ,SUM(payment_amount) AS "Payment Amount"
								  ,payment_type AS "Payment Type"

							FROM	payments

							GROUP BY	date_recorded
										,payment_type

							ORDER BY	date_recorded

		               """)
		results = cursor.fetchall()
		connection.close()

		return results


# Variables.

#interest_to_be_paid = financed_amount * interest_rate
#financed_and_interest = financed_amount + interest_to_be_paid

print('Total Amount to be paid: {0}\n'.format(TOTAL_AMOUNT))

#print('Interest amount to be paid: {0}\n'.format(financed_and_interest - financed_amount))

print('Total days between start and end: {0}\n'.format(NUMBER_OF_DAYS_TOTAL))

start_date = datetime(2020, 6, 19)

next_date = start_date + timedelta(14)

# Get payments remaining.
# Payments remaining will be the remaining divided by the biweekly payment.

# Log when lump sum payments occurred.  Payment type.

print('Total amount to be paid: {0}\n'.format(BIWEEKLY_PAYMENT * NUMBER_OF_PAYMENTS))

print('Payments start on: {0}\n'.format(start_date))

print ('Next payment date: {0}\n'.format(next_date))

program_check = ''

while program_check != 'N':

	while True:

		user_action = int(input('What would you like to do?\n'
	 								'1. View remaining balance.\n'
	 								'2. Apply a lump sum balance.\n'
	 								'3. View payments made.\n'
	 								'4. Quit\n'))

		acceptable_responses = [1, 2, 3, 4]

		if user_action in acceptable_responses:
			if user_action == 1:
				remaining_balance = remainingBalance()
				print('You have paid: ${:,.2f}\n'.format(remaining_balance[0]))
				print('You have ${:,.2f} remaining to pay.'.format(TOTAL_AMOUNT - remaining_balance[0]))
				break

			elif user_action == 2:
				lump_sum_amount = int(input('How much would you like to pay?\n'))
				makePayment(lump_sum_amount)
				break

			elif user_action == 3:
				view_payments_made = viewPaymentsMade()

				for item in view_payments_made:
					print(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]))

				break

			elif user_action == 4:
				exit()

		else:
			print('Please try again.')





