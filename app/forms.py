from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

GENDER_CHOICES = ['', 'Male', 'Female', 'Prefer Not to Answer']

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	gender = SelectField('Gender', choices=GENDER_CHOICES, validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Submit')

	#birthdate
	#email

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


