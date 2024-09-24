# 300 - Creating and Interacting with the Question Model

== WE ARE HERE https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy ==

You’ve created a posts model and interacted with it in your posts blueprint. You will now add the questions database model for managing questions and answers.

At this point in the tutorial, your ```flask_app``` directory structure is as follows (including the virtual environment’s directory):

```
.
├── flask_app
|    ├── .venv
|    ├── app
|    |   ├── __init__.py
|    |   ├── extensions.py
|    |   ├── main
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── models
|    |   │   └── post.py
|    |   ├── posts
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── questions
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   └── templates
|    |       ├── base.html
|    |       ├── index.html
|    |       ├── posts
|    |       |   ├── categories.html
|    |       |   └── index.html
|    |       └── questions
|    |           └── index.html
|    ├── config.py
|    ├── instance
|    |   └── app.db
|    └── requirements.txt
└── README.md
```



MORE