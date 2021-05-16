# aliases :microphone:

##### `About`:
Aliases is a web-app , built with Python using the Django framework, that stores Russell Jone's known rap aliases in an SQLite database and will display a random one using a refresh button.  The app features login functionality that allows a user to add an alias to the database.

---

##### `Requirements`:
* Python 3.9
* pipenv 2020.11.15

---

##### `To Run Locally`:
* In a terminal window `cd ` into the root (Pipfile.lock) directory, create a virtual environment and install developer dependencies (Django):
	`pipenv install --dev`
* Activate the virtual environment:
	`pipenv shell`
* `cd` into project directory (manage.py) and start the Django server:
	`python3 manage.py`
* In a browser (preferably Google Chrome), navigate to:
	`http://localhost:8000/`
