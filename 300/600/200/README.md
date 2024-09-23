# 200 - Creating and Interacting with the Post Model

  == WE ARE HERE https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy ==

In large applications, you may have hundreds of database tables, which means you would need to write hundreds of SQLAlchemy models to manage them. Putting all your models in one file will make your application hard to maintain, so you will split your models into separate Python files inside a models directory. Each file will hold the models and functions related to a specific part of your application. For example, you may put models and functions for managing posts inside a post.py file in a directory called models in the app directory.

At this point in the tutorial, your flask_app directory structure is as follows (excluding the virtual environment’s directory):

```
.
├── flask_app
|    ├── .venv
|    ├── app
|    |   ├── __init__.py
|    |   ├── extensions.py
|    |   ├── instance
|    |   │   └── app.db
|    |   ├── main
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── posts
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── questions
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   └── templates
|    |           ├── base.html
|    |           ├── index.html
|    |           ├── posts
|    |           |   ├── categories.html
|    |           |   └── index.html
|    |           └── questions
|    |               └── index.html
|    ├── config.py
|    └── requirements.txt
└── README.md
```

To create a database model for posts in its own file, first create a directory called ```models``` inside your ```app``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ mkdir app/models
```

Then, open a new file called ```post.py``` inside your ```models``` directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/models/post.py
```

Add the following code to the newly created file:

```
#!/usr/bin/env python
from app.extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post "{self.title}">'
```
flask_app/app/models/post.py

Save and close the file.

You import the ```db``` database object from the ```app.extensions``` module. Then you create a Flask-SQLAlchemy database model called ```Post``` using the ```db.Model``` class. In the model, you have an ID integer column as a primary key (```id```), a column to hold strings for the post title (```title```), and a text column for content (```content```). You use the special ```__repr__()``` method to provide a string representation for each post object using its title. For more on Flask-SQLAlchemy, you can review [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application).

Next, open the Flask shell to create the post table based on the post model:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ flask shell
```

Run the following code to create the posts table:

```
>>> from app.extensions import db
>>> from app.models.post import Post
>>> db.create_all()
```

You import the ```db``` object from the ```app.extensions``` module and the ```Post``` model from the ```app.models.post``` module. Then you use the ```create_all()``` method to create the posts table.

The code should execute without an output. If you receive an error, check your ```app/extensions.py``` and ```app/models/post.py``` files, and review the previous steps to ensure you have followed them as written.

**Note**: A file called ```app.db``` should appear in ```flask-app/app/instance/``` directory.

**Note**: 

MORE