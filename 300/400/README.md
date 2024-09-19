# 400 - Creating a Flask Application Factory

== WE ARE HERE: https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#step-3-creating-a-flask-application-factory ==

In this step, you’ll create a [Flask application factory](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/), which is a Python function that sets up a Flask application instance.

At this point in the tutorial, your ```app``` directory structure is as follows (excluding the virtual environment’s directory):

```
.
├── app
|   └── requirements.txt
└── config.py
```

Your application’s core code will live inside a project directory, which will be a Python package. In this tutorial, we’ll call it ```app```, but you can use your project’s name or another common directory name such as ```src```, ```core```, or something similar.

You’ll make the folder containing the application’s core code a Python package so that imports work correctly throughout the code base and to increase its maintainability.

To make the ```app``` project directory a Python package, you’ll create a special ```__init__.py``` file inside of it, which marks directories as Python packages. This ```__init__.py``` file will hold code for your *Flask factory function*, which is a function you’ll use to set and create the Flask application instance where you link all your Flask blueprints together. Think of the factory function as the central function in which all your Flask components (blueprints) are combined into one application and that you can use to create different Flask application instances for different purposes with different configurations. For example, you could use the factory function to create a Flask application instance for testing with proper configurations for testing.

Create a file named ```__init__.py``` inside the ```app``` directory and add the following code to it:

```
#!/usr/bin/env python
from flask import Flask
from config import Config

def create-app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
```
app/__init__.py

Save and close the file.

In this file, you import the ```Flask``` class from the ```flask``` package. Then you import the ```Config``` configuration class from the ```config.py``` file you created outside the ```app``` directory, in the root directory, in the previous step.

The ```create_app()``` function is the [Flask application factory function](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/). It creates an application instance called ```app``` from the ```Flask()``` class using the familiar ```app = Flask(__name__)``` line. You configure the application by importing configuration values from an object using the ```app.config.from_object()``` method, passing it the value of the ```config_class``` parameter, which holds the ```Config``` class as a default value. You will initialize your Flask extensions below the ```# Initialize Flask extensions here``` comment and register your application blueprints below the ```# Register blueprints here``` comment once you create them.




MORE