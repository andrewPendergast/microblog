from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Andrew'}
	posts = [
		{
			'author': { 'nickname': 'Andrew' },
			'body': 'Beautiful day at Domi!'
		},
		{
			'author': { 'nickname': 'Carolyn' },
			'body': 'Missing the Domi station!'
		},
                {
                        'author': { 'nickname': 'William' },
                        'body': 'Super excited about Proper Channel'
                }
	]
	return render_template('index.html',
				title='Home',
				user=user,
				posts=posts)
