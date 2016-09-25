from flask import Flask

app = Flask(__name__)
#creates an application object of class Flask

app.config.from_object('config')
#tells app to read and use config.py

from app import views
#imports views module
