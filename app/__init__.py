from flask import Flask, request, render_template, redirect
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# print(app.config['SECRET_KEY'])
workouts = {
    1: {
        'id': 1,
        'title': 'Mountain Run',
        'duration': 90,
        'exertion_level': 'Moderate',
    }
}


@app.route('/')
def index():
    """
    A simple route to display all workouts
    """
    workouts_list = [workout for workout in workouts.values()]
    return render_template('index.html', workouts=workouts_list)


@app.route('/workouts/<int:id>')
def get_single_workout(id):
    """
    Shows a single Form
    """
    return render_template('show.html', workout=workouts[id])
