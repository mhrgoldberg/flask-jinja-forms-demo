from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# print(app.config['SECRET_KEY'])


@app.route('/')
def index():
	"""
	A simple route to display all workouts
	"""
	return "<h1>My Workouts</h1>"

