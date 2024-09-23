# 300 - Creating the Questions Blueprint and Rendering its Templates

Now you’ll create the questions blueprint, register it, and render its templates.

At this point in the tutorial, your ```flask_app``` directory structure is as follows (including the virtual environment’s directory):

```
.
├── flask_app
|    ├── .venv
|    ├── app
|    |   ├── __init__.py
|    |   ├── instance
|    |   │   └── app.db
|    |   ├── main
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── posts
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   └── templates
|    |           ├── base.html
|    |           ├── index.html
|    |           └── posts
|    |               ├── categories.html
|    |               └── index.html
|    ├── config.py
|    └── requirements.txt
└── README.md
```

To create a new blueprint for questions and answers, create a new ```questions``` directory to hold the blueprint’s files:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/questions
```

Next, open a new ```__init__.py``` file inside the new ```questions``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/questions/__init__.py
```

Create a ```bp``` blueprint object and import the routes that you’ll later create in the blueprint’s ```routes.py``` file:

```python title="__init__.py"
#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('questions', __name__)

from app.questions import routes
```
flask_app/app/questions/__init__.py

Save and close the file.

In the preceding code block, you use ```questions``` as the blueprint’s name. You also import the routes from a ```routes.py``` file, which you haven’t created yet.

Next, open the new ```routes.py``` file where you’ll put the routes for the questions blueprint:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/questions/routes.py
```

Add the following routes to this file:

```python title="routes.py"
#!/usr/bin/env python
from flask import render_template
from app.questions import bp

@bp.route('/')
def index():
    return render_template('questions/index.html')
```
flask_app/app/questions/routes.py

Save and close the file.

You create a ```/``` route using the ```questions``` blueprint object, rendering a template file called ```index.html``` inside a directory called ```questions```, which you’ll create inside the templates folder.

Create the ```questions``` directory inside the templates directory, and then open an ```index.html``` file in it:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/templates/questions
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/questions/index.html
```

Add the following code to the new file:

```html title="index.html"
{% extends 'base.html' %}

{% block content %}
    <span class="title">
        <h1>{% block title %} Questions {% endblock %}</h1>
    </span>
    <div class="questions">
        <h2>Questions Blueprint</h2>
    </div>
{% endblock %}
```
flask_app/app/templates/questions/index.html

Save and close the file.

Here, you set a title and a subheading, similar to the previous index templates in the other blueprints.

Now open ```app/__init__.py``` to register the questions blueprint in the ```create_app()``` factory function:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/__init__.py
```

Edit the create_app() factory function by adding the highlighted lines:

```
#!/usr/bin/env python
from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

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

Save and close the file.

You register the questions blueprint as you did with the posts blueprint, adding a ```/questions``` prefix to its routes.

With your development server running, use your browser to navigate to the following URL (**Note**: You may have to stop and start your server):

```
http://127.0.0.1:5000/questions/
```

The **Questions** and **Questions Blueprint** headings will be displayed on the page.

You will now make the **Questions** link functional. Open the base template to edit the navigation bar:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/base.html
```

Modify the <nav> tag with the highlighted expression:

```
...
<nav>
        <a href="{{ url_for('main.index') }}">FlaskApp</a>
        <a href="{{ url_for('posts.index') }}">Posts</a>
        <a href="{{ url_for('posts.categories') }}">Categories</a>
        <a href="{{ url_for('questions.index') }}">Questions</a>
</nav>
...    
```
flask_app/app/templates/base.html

Save and close the file.

Here, you link to the questions index page using the ```url_for('questions.index')``` function call.

Refresh any page in your application to enable the **Questions** link functionality in the navigation bar.

You have created several blueprints to manage different components of your application. You registered the blueprints on your factory function and rendered templates for each route. Next, you’ll add Flask-SQLAlchemy to your application to manage and organize large databases in your Flask application.