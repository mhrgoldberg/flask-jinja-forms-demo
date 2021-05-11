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
	print([workouts[id]])
	return render_template('show.html', workout=workouts[id] )


@app.route('/workouts/new')
def get_workout_form():
	"""
	Serves up a new_workout form template
	"""
	return render_template('new.html')
	

@app.route('/workouts/new', methods=['POST'])
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