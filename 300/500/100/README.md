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
flask_app/app/main/\_\_init\_\_.py

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

Add the import line at the end of the file:

```python title="__init__.py"
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
```
flask_app/app/main/\_\_init\_\_.py

Save and close the file.

With this addition, registering a blueprint will also register its routes.

Now that you’ve created a blueprint and added a route, you’ll need to tell Flask about this new blueprint so that it can be treated as part of your Flask application. To do this, you’ll register the blueprint inside your Flask application factory function.

Open the flask_app/app/__init__.py file to edit your factory function:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/__init__.py
```

Edit the ```create_app()``` factory function to match the following block, adding the highlighted lines:

```python title="__init__.py"
...
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
```
flask_app/app/__init__.py

Save and close the file.

You import the ```bp``` blueprint object from the main blueprint and rename it to ```main_bp``` for readability. Then you use the ```app.register_blueprint()``` method to register this main blueprint for Flask to treat as part of the application.

With the development server running, navigate to the following URL:

```
http://127.0.0.1:5000
```

The page will load with the text **This is The Main Blueprint**, which is the text you returned in the main route.

You now have a blueprint with a route in your application. Next, you will edit the main route in the main blueprint to render an HTML template, which will demonstrate how to render templates when working with Flask blueprints.

Open the ```routes.py``` file of the main blueprint for modification:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/main/routes.py
```

Edit the file as follows:

```python title="routes.py"
#!/usr/bin/env python
from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')
```
flask_app/app/main/routes.py

Save and close the file.

Here, you import the ```render_template()``` function and use it in the route to render a template file called ```index.html```.

You’ll now have to create a templates directory and base template that all other templates will share to avoid code repetition.

Create a templates directory inside your ```app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/templates
```

Open a new file called ```base.html``` to act as the base template:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/base.html
```

Add the following code to the new file:

```html title="base.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %} {% endblock %} - FlaskApp</title>
    <style>
        h2 {
            width: 100%;
        }

        .title {
            margin: 5px;
            width: 100%;
        }

        .content {
            margin: 5px;
            width: 100%;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
        }

        .post {
            flex: 20%;
            padding: 10px;
            margin: 5px;
            background-color: #f3f3f3;
            inline-size: 100%;
        }

        .title a {
            color: #00a36f;
            text-decoration: none;
        }

        nav a {
            color: #d64161;
            font-size: 3em;
            margin-left: 50px;
            text-decoration: none;
        }

    </style>
</head>
<body>
    <nav>
        <a href="{{ url_for('main.index') }}">FlaskApp</a>
        <a href="#">Posts</a>
        <a href="#">Categories</a>
        <a href="#">Questions</a>
    </nav>
    <hr>
    <div class="content">
        {% block content %} {% endblock %}
    </div>
</body>
</html>
```
flask_app/app/templates/base.html

Save and close the file.

This base template features HTML boilerplate that you will reuse in your other templates.

The base template has a title block, some CSS, a navigation bar to link to different parts of your application, and a content block. For more on base templates, see [How To Use Templates in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application).

You use the syntax ```blueprint_name.view_function_name``` to link to a route when using the ```url_for()``` function with blueprints. The index page is handled by the ```index()``` view function in the main blueprint; therefore, you pass ```main.index``` to the ```url_for()``` function to build a link.

Now, create the ```index.html``` file you rendered in the ```index()``` view function of the main blueprint:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/index.html
```

Add the following code to the newly created file:

```html title="index.html"
{% extends 'base.html' %}

{% block content %}
    <span class="title"><h1>{% block title %} The Home Page of FlaskApp {% endblock %}</h1></span>
    <div class="content">
        <h2>This is the main Flask blueprint</h2>
    </div>
{% endblock %}
```
flask_app/app/templates/index.html

Save and close the file.

Here, you extend the base template. You replace the content block, using an ```<h1>``` heading that also serves as a title and an ```<h2>``` heading to indicate the index page is part of the main Flask blueprint.

With the development server running, visit the index page using your browser or refresh it if it’s already open (**Note**: You may have to stop and start your server):

```
http://127.0.0.1:5000/
```

A page similar to the following image will load:

![image](https://github.com/user-attachments/assets/1812ce0e-ef50-4a8b-9f62-7169747de30a)

You have now set up a blueprint, added a route to its ```routes.py``` file, registered it on the application, and rendered templates for it. Next, you’ll create another blueprint for blog posts.
