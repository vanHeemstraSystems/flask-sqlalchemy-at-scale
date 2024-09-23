# 100 - Creating the Main Blueprint and Rendering its Templates

You will now create the main blueprint for the application and render its templates.

Leave the development server you started in the previous step running, and open a new terminal.

Navigate to your ```flask_app``` directory in the new terminal. Then create a directory called ```main``` for your main blueprint inside the ```app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/main
```

Next, open a new ```__init__.py``` main file inside the new main directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/main/__init__.py
```

This is where you’ll create your main blueprint. Add the following code to this file:

```
#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('main', __name__)
```
flask_app/app/main/__init__.py

Save and close the file.

Here, you import the [Blueprint](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Blueprint) class from the ```flask``` package. Then you use this class to create a blueprint object ```bp```, passing it two arguments: a name (```'main'``` in this case) and the ```__name__``` special variable, which holds the name of the current Python module.

You now have a blueprint object, which will later have routes and functions you can plug into the Flask application you create using the ```create_app()``` factory function you’ve written in the previous step.

Next, you’ll create a ```routes.py``` file inside your ```main``` blueprint directory, which will hold the routes of the main blueprint. Open a new ```routes.py``` file inside your main blueprint directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/main/routes.py
```

You’ll create routes using the ```bp``` object. Add the following route inside the new file:

```
#!/usr/bin/env python
from app.main import bp

@bp.route('/')
def index():
    return 'This is The Main Blueprint'
```
flask_app/app/main/routes.py

Save and close the file.

Here, you import the ```bp``` blueprint object from the main blueprint, which you access through ```app.main```. In the import line, ```app``` is the project’s package, ```main``` is the main blueprint package, and ```bp``` is the object you declared in the main blueprint’s ```__init__.py``` file.

You use the ```bp``` object to create a ```/``` route and an ```index()``` view function with the ```bp.route()``` decorator, similar to the familiar ```app.route()``` decorator.

For Flask to use these routes and to make them importable directly from the blueprint, you’ll need to import this ```routes.py``` file in your blueprint’s ```__init__.py``` file. Open it for editing:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/main/__init__.py
```

Add the highlighted import line at the end of the file:

```python title="__init__.py"
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
```
flask_app/app/main/__init__.py

Save and close the file.

With this addition, registering a blueprint will also register its routes.

Now that you’ve created a blueprint and added a route, you’ll need to tell Flask about this new blueprint so that it can be treated as part of your Flask application. To do this, you’ll register the blueprint inside your Flask application factory function.

Open the app/__init__.py file to edit your factory function:

MORE