from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class WorkoutForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    duration = IntegerField("Duration")
    exertion_level = SelectField(
        "Exertion Level",
        choices=["Easy", "Moderate", "Hard"]
    )
    submit = SubmitField("Create Workout")
