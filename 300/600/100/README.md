# 100 - Creating a File for Managing Flask Extensions and Integrating Flask-SQLAlchemy

To add the Flask-SQLAlchemy extension to your application, you’ll first add a Python module called ```extensions.py```, in which you’ll set up your various Flask extensions, to your ```app``` directory.

Open a new ```extensions.py``` file inside your app directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/extensions.py
```

Add the following code to the newly created file:

```
#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```
flask_app/app/extensions.py

Save and close the file.

Here, you import the ```SQLAlchemy()``` class from the Flask-SQLAlchemy package, and then you use it to create a ```db``` database object with no arguments.

You will use this ```db``` object to integrate SQLAlchemy with the Flask application you construct in your factory function. Open your ```app/__init__.py``` file to edit the factory function:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/__init__.py
```

Edit the file to import and initialize the database object:

```
#!/usr/bin/env python
from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
```
flask_app/app/__init__.py

Here, you import the ```db``` database object from the ```app.extensions``` module you created earlier. Before registering blueprints, you connect the database object to the ```app``` application instance using the ```db.init_app()``` method. With this, you can use your ```db``` object to create and interact with Flask-SQLAlchemy models in your application.

Remember that you’ve configured Flask-SQLAlchemy using the ```Config``` object in the ```config.py``` file inside your ```flask_app``` directory. You can open this file for a quick reminder:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano config.py
```

```
#!/usr/bin/env python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
flask_app/app/config.py

If you don’t set up a ```DATABASE_URI``` environment variable, the ```db``` object will, by default, connect to an SQLite file called ```app.db``` that will appear in your ```flask_app/instance/``` directory once you create your database tables. Close the file when finished reviewing it.

You can check that the database was registered correctly using the Flask shell. First, with your virtual environment activated, make sure you’ve set up your Flask environment variables in your ```flask_app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ export FLASK_APP=app
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ export FLASK_ENV=development
```

Open the Flask shell:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ flask shell
```

Import the db object from the app.extensions module, then print it:

```
>>> from app.extension import db
>>> print(db)
```

You’ll receive the path of your database, similar to the following:

```
<SQLAlchemy sqlite:////workspace/flask-sqlalchemy-at-scale/flask_app/instance/app.db>
```

This output means that the ```db``` object was properly registered. If you get an error running the code in the Flask shell, ensure you’ve correctly registered the ```db``` object in your factory function before moving to the next section. You can exit the Flask shell by typing ```exit()```.