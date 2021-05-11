from flask import Blueprint, render_template, request, redirect


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


@workout_routes.route('/new')
def get_workout_form():
	"""
	Serves up a new_workout form template
	"""
	return render_template('new.html')
	

@workout_routes.route('/new', methods=['POST'])
def add_new_workout():
	"""
	Validates form data and adds to DB
	"""
	form_data = request.form

	if (
		form_data['title'] and 
		form_data['duration'] and 
		form_data['exertion_level']
		):
		i = len(workouts) + 1
		new_workout = {
			'id': i,
			'title': form_data['title'],
			'duration': int(form_data['duration']),
			'exertion_level': form_data['exertion_level']
		}
		workouts[i] = new_workout
		print(workouts)
		return redirect(f'/workouts/{i}')
	return "There was a error submiting your form. Please try again!"