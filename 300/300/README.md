## 300 - Creating a Configuration File

In this step, you’ll create a configuration file for your Flask application, separating your application settings from the rest of the application and making changing settings easier. The configuration file will configure things such as [the secret key](https://flask.palletsprojects.com/en/2.2.x/api/#sessions), the [SQLAlchemy database URI](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application#step-2-setting-up-the-database-and-model), and so on.

In your ```flask_app``` directory, open a new file called ```config.py```. This file will hold your Flask application’s configuration:

```python title="config.py"
#!/usr/bin/env python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
flask_app/config.py

Save and close the file.

You import the ```os``` module to access your file system.

You use a class called ```Config``` and set configuration values using class variables. Here, you set three configurations:

- ```SECRET_KEY```: A long random string used by Flask as a secret key, or a key used to secure the sessions that remember information from one request to another. The user can access the information stored in the session but cannot modify it unless they have the secret key, so you must never allow anyone to access your secret key. See the [Flask documentation on sessions](https://flask.palletsprojects.com/en/2.2.x/api/#sessions) for more information. Other Flask extensions often use this secret key to secure data. See [Step 3 of How To Use Web Forms in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-3-handling-form-requests) for more information on how to create a secure secret key. When developing your Flask applications, you should set the secret key with an environment variable called ```SECRET_KEY```. To get its value in this ```config.py``` file and save it in a class variable called ```SECRET_KEY```, you access the environment variable’s value via the [os.environ](https://docs.python.org/3/library/os.html#os.environ) object using its ```get()``` method. (Though you do not need to set a secret key to follow this tutorial, you can review the note at the end of this list for instructions on how to set a secret key.)

- ```SQLALCHEMY_DATABASE_URI```: The database URI specifies the database you want to establish a connection with using SQLAlchemy. In this case, you either get it from a ```DATABASE_URI``` environment variable or you set a default value. The default URI value here follows the format ```sqlite:///app.db```. With this, creating a Flask application without setting a ```DATABASE_URI``` environment variable will connect to an ```app.db``` database file in your ```app/instance``` directory by default. The file will be created when you create your database tables. If you’d like to set a database URI for a different SQL engine, see [Step 2 of How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application#step-2-setting-up-the-database-and-model).

- ```SQLALCHEMY_TRACK_MODIFICATIONS```: A configuration to enable or disable tracking modifications of objects. You set it to ```False``` to disable tracking and use less memory. For more, you can read [the configuration page](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) in the Flask-SQLAlchemy documentation.

**Note**: You will not set a secret key in this tutorial because you will not use functionality that needs a secret key. However, if you need to set a secret key, you can set it as follows (for Windows, use ```set``` instead of ```export```):

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ export SECRET_KEY=" your secret key "
```

Similarly, you can set a database URI like so (use set on Windows):

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ export DATABASE_URI="postgresql:// username : password @ host : port / database_name "
```

You have now set up a configuration file for your application. Next, you’ll set up a Flask application instance and create a few blueprints that represent different components of your Flask application.