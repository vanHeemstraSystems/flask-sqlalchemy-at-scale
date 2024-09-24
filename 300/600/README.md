# 600 - Adding Flask-SQLAlchemy Models to your Flask Application

In this step, you’ll integrate Flask-SQLAlchemy with your application, add a directory for database models, and create a model for posts and one for questions. You’ll insert a few blog posts into the posts table, then edit the posts’ index route to display all posts in the database. You will also insert a few questions and answers into the questions table to display them on the questions’ index page, alongside a new web form for adding further questions and answers to the database.

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

## 100 - Creating a File for Managing Flask Extensions and Integrating Flask-SQLAlchemy

See [README.md](./100/README.md)

## 200 - Creating and Interacting with the Post Model

See [README.md](./200/README.md)

## 300 - Creating and Interacting with the Question Model

See [README.md](./300/README.md)

MORE