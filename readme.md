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
