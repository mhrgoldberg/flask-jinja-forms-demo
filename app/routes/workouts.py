from flask import Blueprint, render_template


workout_routes = Blueprint('workouts', __name__, url_prefix='/workouts')

workouts = {
    1: {
        'id': 1,
        'title': 'Mountain Run',
        'duration': 90,
        'exertion_level': 'Moderate',
    }
}


@workout_routes.route('/')
def index():
    """
    A simple route to display all workouts
    """
    workouts_list = [workout for workout in workouts.values()]
    return render_template('index.html', workouts=workouts_list)


@workout_routes.route('/<int:id>')
def get_single_workout(id):
    """
    Shows a single Form
    """
    print([workouts[id]])
    return render_template('show.html', workout=workouts[id])
