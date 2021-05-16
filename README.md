# aliases :microphone:

##### `About:`
Aliases is a web-app , built with Python using the Django framework, that stores Russell Tyrone Jones' known rap aliases in an SQLite database. The main page displays a random alias and includes a refresh button for accessing random aliases.  The app features login functionality that allows a user to add an alias to the database.

---

##### `Requirements:`
* Python 3.9
* pipenv 2020.11.15

---

##### `To Run Locally:`
* In a terminal window `cd` into the root directory (Pipfile.lock), create a virtual environment and install developer dependencies (Django):
	`pipenv install --dev`
* Activate the virtual environment:
	`pipenv shell`
* `cd` into project directory (manage.py) and start the Django server:
	`python3 manage.py runserver`
* In a browser (preferably Google Chrome), navigate to:
	`http://localhost:8000/`
