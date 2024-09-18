## 300 - Creating a Configuration File

In this step, you’ll create a configuration file for your Flask application, separating your application settings from the rest of the application and making changing settings easier. The configuration file will configure things such as [the secret key](https://flask.palletsprojects.com/en/2.2.x/api/#sessions), the [SQLAlchemy database URI](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application#step-2-setting-up-the-database-and-model), and so on.

In your ```app``` directory, open a new file called ```config.py```. This file will hold your Flask application’s configuration:

MORE