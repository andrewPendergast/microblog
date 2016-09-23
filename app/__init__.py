from flask import Flask

app = Flask(__name__)
#creates an application object of class Flask
from app import views
#imports views module
