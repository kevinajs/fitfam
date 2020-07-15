from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Display this shit')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form = form)
