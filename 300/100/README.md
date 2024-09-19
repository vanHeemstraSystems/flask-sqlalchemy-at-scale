# 100 - The Target Application Structure

By the end of the tutorial, you will have built a Flask application with the following structure:

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
|    |   ├── models
|    |   │   ├── post.py
|    |   │   └── question.py
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
|    |           │   ├── categories.html
|    |           │   └── index.html
|    |           └── questions
|    |               └── index.html
|    ├── config.py
|    └── requirements.txt
└── README.md
```

Inside your ```flask_app``` directory, you’ll have a ```config.py``` configuration file for your Flask application and a requirements file for the Python packages required. The main Flask application will be in the ```app``` directory, which will have an ```__init__.py``` special file to make it a package for imports to work properly, and it will contain a function for creating the Flask application instance.

The ```app``` directory will contain an ```extensions.py``` file for managing the Flask extensions you’ll use in your application (in this tutorial, Flask-SQLAlchemy is the example of using a Flask extension). You will also have the following directories:

- ```main```: the main blueprint for main routes, such as the home page.
- ```models```: the directory that will contain Flask-SQLAlchemy models.
- ```posts```: the posts blueprint for managing blog posts.
- ```questions```: the questions blueprint for managing questions and answers.
- ```templates```: the templates directory that will contain files for the main blueprint and a directory for each blueprint.