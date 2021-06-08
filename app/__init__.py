from flask import Flask, render_template
from app.config import Config
from .routes import workout_routes, workouts

app = Flask(__name__)
app.config.from_object(Config)

# print(app.config['SECRET_KEY'])


@app.route('/')
def index():
    return "Go to /workouts to use the app!"


app.register_blueprint(workout_routes)
