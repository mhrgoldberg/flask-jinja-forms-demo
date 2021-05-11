from flask import Blueprint, render_template, request, redirect
from app.forms import WorkoutForm

workout_routes = Blueprint('workouts', __name__, url_prefix='/workouts')

workouts = {
	1: {
		'id': 1,
		'title': 'Mountain Run',
		'duration': 90,
		'exertion_level': 'Moderate',
	}
}



@workout_routes.route('/<int:id>')
def get_single_workout(id):
	"""
	Shows a single Form
	"""
	print([workouts[id]])
	return render_template('show.html', workout=workouts[id] )


# @workout_routes.route('/new')
# def get_workout_form():
# 	"""
# 	Serves up a new_workout form template
# 	"""
# 	form = WorkoutForm()
# 	return render_template('new.html', form=form)
	

@workout_routes.route('/new', methods=['GET', 'POST'])
def add_new_workout():
	"""
	Validates form data and adds to DB
	"""
	form = WorkoutForm()

	if form.validate_on_submit():
		i = len(workouts) + 1
		new_workout = {
			'id': i,
			'title': form.data['title'],
			'duration': form.data['duration'],
			'exertion_level': form.data['exertion_level']
		}
		workouts[i] = new_workout
		print(workouts)
		return redirect(f'/workouts/{i}')

	return render_template('new.html', form=form)
