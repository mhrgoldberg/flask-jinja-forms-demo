# W18D2 Lecture Repo

## Local Setup

1. First run the below to install the required dependencies located in the provided pipfile:

   ```bash
   pipenv install
   ```

2. Enter the virtual environment shell

   - This step will initialize your .env variables into flask

   ```bash
   pipenv shell
   ```

3. Run the app

   ```bash
   flask run
   ```

4. Go to localhost:5000 to see the app in action

## Jinja

1. Install jinja2 locally with:
   ```bash
   pipenv install jinja2
   ```
2. Create `templates` directory in the app module
3. Update `get` route to use a Jinja index template
4. Create `post` route to create a workout
5. Create a `new_workout` template

## Blueprints

1. Create a `routes` directory in the app module
2. add `workouts.py` file and move routes from app over
3. add `__init__.py` file and import workouts.py
4. Import `routes` module into the app `__init__` and register the blueprint

## Forms

1. Install flask_wtf

```bash
pipenv install flask_wtf
```

1. Create a `forms` directory in the app module
2. create `workout_form.py` in the directory
3. create `__init__.py` and import the workout_form
4. Import form into routes and refactor the routes to utilize the forms
