from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Rods'}
	title = 'Hooplah'
	posts = [
		{
			'author': {'username': 'Kim'},
			'body': 'Bodacious'
		},
		{
			'author': {'username': 'Kevin'},
			'body': 'Solid steals'
		}
			]
	return render_template('index.html',
	                       user=user,
	                       title=title,
	                       posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember me={}'.format(
		                                                            form.username.data,
		                                                            form.remember_me.data
		                                                            ))
		return redirect('/index')

	return render_template(url_for('index'),
	                       title='Log In',
	                       form=form)
