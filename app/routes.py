from flask import render_template
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Display this shit')

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('registration.html', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
