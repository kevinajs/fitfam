from datetime import datetime

class User(object):
	def __init__(self):
		self.username = input('What would you like your username to be?\n')
		self.password = input('What would you like your password to be?\n')
		self.email = input('Key in your e-mail address.\n')
		self.created_on = datetime.today()
		self.last_login = datetime.today()
