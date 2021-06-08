<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
>>>>>>> 3-forms
from app.config import Config
from .routes import workout_routes

app = Flask(__name__)
app.config.from_object(Config)

# print(app.config['SECRET_KEY'])

<<<<<<< HEAD
=======

>>>>>>> 3-forms
@app.route('/')
def index():
    return "Go to /workouts to use the app!"


app.register_blueprint(workout_routes)
