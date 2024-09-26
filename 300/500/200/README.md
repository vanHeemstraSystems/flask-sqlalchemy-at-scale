# 200 - Creating the Posts Blueprint and Rendering its Templates

Now you’ll create the blueprint for blog posts, register it, and render its templates.

At this point in the tutorial, your flask_app directory structure is as follows (including the virtual environment’s directory):

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
|    |   └── templates
|    |           ├── base.html
|    |           └── index.html
|    ├── config.py
|    └── requirements.txt
└── README.md
```

To create a new blueprint for blog posts, you’ll follow the same steps as in the previous section.

First, create a new ```posts``` directory to hold the blueprint’s files:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/posts
```

Next, open a new ```__init__.py``` file inside the new ```posts``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/posts/__init__.py
```

Create a ```bp``` blueprint object and import the routes that you’ll create into the blueprint’s ```routes.py``` file:

```python title="__init__.py"
#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('posts', __name__)

from app.posts import routes
```
flask_app/app/posts/\_\_init\_\_.py

Save and close the file.

In the preceding code block, you use ```posts``` as the blueprint’s name. You also import the routes from a ```routes.py``` file, which you haven’t created yet.

Next, open the new ```routes.py``` file where you’ll put the routes for the posts blueprint:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/posts/routes.py
```

Add the following routes to this file:

```python title="routes.py"
#!/usr/bin/env python
from flask import render_template
from app.posts import bp

@bp.route('/')
def index():
    return render_template('posts/index.html')

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')
```
flask_app/app/posts/routes.py

Save and close the file.

Here, you have two routes: a route for the index page of the posts component of the application and a route for categories, which will be part of the posts component.

In the ```index``` route, you render a template file with the path ```posts/index.html``` which means that Flask will look for a directory called ```posts``` in the ```templates``` directory and then look for an ```index.html``` file inside of the ```posts``` directory.

In the ```categories``` route, you render a ```categories.html``` template, which will also be inside a ```posts``` directory inside the ```templates``` folder.

Now create the new ```posts``` directory inside your templates directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/templates/posts
```

Next, create the new ```index.html``` file inside the ```templates/posts``` directory. This is the file you render in the ```index()``` view function of the posts blueprint:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/posts/index.html
```

Add the following code to the newly created file:

```python title="index.html"
{% extends 'base.html' %}

{% block content %}
    <span class="title"><h1>{% block title %} The Posts Page {% endblock %}</h1></span>
    <div class="content">
        <h2>This is the posts Flask blueprint</h2>
    </div>
{% endblock %}
```

Save and close the file.

Here you extend the base template. You also set an ```<h1>``` heading as a title and an ```<h2>``` heading to mark the page as part of the posts blueprint.

Next, create a new ```categories.html``` file inside the ```posts``` directory. This is the file you rendered in the ```categories()``` view function of the posts blueprint:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/posts/categories.html
```

Add the following code to the newly created file:

```python title="categories.html"
{% extends 'base.html' %}

{% block content %}
    <span class="title"><h1>{% block title %} Categories {% endblock %}</h1></span>
    <div class="content">
        <h2>This is the categories page within the posts blueprint</h2>
    </div>
{% endblock %}
```
flask_app/app/templates/posts/categories.html

Save and close the file.

You extend the base template and set an ```<h1>``` heading as a title and a ```<h2>``` heading to mark the page as part of the posts blueprint.

You’ve created the posts blueprint, added routes, and made the rendered templates. You will now register this blueprint in your factory function for Flask to recognize it as part of the application.

Open the ```app/__init__.py``` file to edit your factory function:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/__init__.py
```

Edit the ```create_app()``` factory function as follows:

```python title="__init__.py"
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

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
```
flask_app/app/__init__.py

Save and close the file.

Here you imported the ```bp``` blueprint object from the posts blueprint package and renamed it ```posts_bp``` for readability.

You register the posts blueprint using the ```app.register_blueprint()``` method by passing it the ```posts_bp``` blueprint object. You also pass it a value ```'/posts'``` for the ```url_prefix``` parameter, which will prefix the blueprint’s routes with this string. For example, the main ```/``` route of the posts blueprint will become accessible via ```/posts/```, and the ```/categories``` route will be at ```/posts/categories/```.

With your new posts blueprint registered and your development server running, use your browser to navigate to the following URLs (**Note**: You may have to stop and start your server):

```
http://127.0.0.1:5000/posts/
http://127.0.0.1:5000/posts/categories/
```

The **The Posts Page** heading will load for the http://127.0.0.1:5000/posts/ page. A **Categories** heading will load for the http://127.0.0.1:5000/posts/categories/ page.

To make the **Posts** and **Categories** links in the navigation bar functional, open the base template for modification:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/base.html
```

Modify the <nav> tag with these expressions:

```html title="base.html"
...
<nav>
        <a href="{{ url_for('main.index') }}">FlaskApp</a>
        <a href="{{ url_for('posts.index') }}">Posts</a>
        <a href="{{ url_for('posts.categories') }}">Categories</a>
        <a href="#">Questions</a>
</nav>
...
```
flask_app/app/templates/base.html

Save and close the file.

You link to the posts index with the ```url_for('posts.index')``` function call and the categories page with ```url_for('posts.categories')```.

Refresh any page in your application to enable the **Posts** and **Categories** link functionality (**Note**: You may have to stop and start your server).

You now have a posts blueprint registered in your application. Next, you’ll add a blueprint for questions and answers.
