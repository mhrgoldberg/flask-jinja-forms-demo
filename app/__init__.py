from flask import Flask, request, render_template, redirect
from app.config import Config
from .routes import workout_routes, workouts

app = Flask(__name__)
app.config.from_object(Config)

# print(app.config['SECRET_KEY'])
@app.route('/')
def index():
	"""
	A simple route to display all workouts
	"""
	workouts_list = [workout for workout in workouts.values()]
	return render_template('index.html', workouts=workouts_list)


app.register_blueprint(workout_routes)
