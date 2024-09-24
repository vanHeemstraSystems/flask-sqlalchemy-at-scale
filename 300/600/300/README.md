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

To create a questions database model, open a new file called ```question.py``` inside your models directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/models/question.py
```

Add the following code:

```python title="question.py"
#!/usr/bin/env python
from app.extensions import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __repr__(self):
        return f'<Question {self.content}>'
```
flask_app/app/models/question.py

Save and close the file.

Here, you import the ```db``` database object from the ```app.extensions``` module. Then you create a model called ```Question``` using the ```db.Model``` class. In the model, you have an ID integer column as a primary key (```id```), a text column for the question’s content (```content```), and a text column for its answer (```answer```). Then you use the special ```__repr__()``` method to represent each question using its content.

In the terminal session that is running the Flask shell, run the following code to create the questions table based on the questions model:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ flask shell
```

Run the following code to create the questions table and add a few questions and answers to it:

```
>>> from app.extensions import db
>>> from app.models.question import Question
>>> db.create_all()
>>>
>>> q1 = Question(content='Why is the sky blue?', answer='Because... Why not?')
>>> q2 = Question(content='What is love?', answer='A portal to the underworld.')
>>> db.session.add_all([q1, q2])
>>> db.session.commit()
```

The code should execute without an output. If you receive an error, check your app/models/question.py file to ensure your code is written with the correct syntax.

You import the database object and the questions model, then use db.create_all() to create the table, and finally you add two question objects to the database session and commit the transaction.

Exit the Flask shell:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ exit()
```

You can now interact with the new questions model in your questions blueprint. To do so, open the questions blueprint’s ```routes.py``` file for a modification to query and display the questions you have in your questions table:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/questions/routes.py
```

Edit the file as follows:

```python title="routes.py"
#!/usr/bin/env python
from flask import render_template
from app.questions import bp
from app.models.question import Question

@bp.route('/')
def index():
    questions = Question.query.all()
    return render_template('questions/index.html', questions=questions)
```
flask_app/app/questions/routes.py

Save and close the file.

Here, you import the questions model, get all the questions in the database, and then pass them to the questions’ index template.

Next, you’ll display the questions you passed to the questions’ index template and add a web form to allow users to add new questions. Open the ```index.html``` file in the questions’ template directory:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/questions/index.html
```

Edit the file as follows:

```html title="index.html"
{% extends 'base.html' %}

{% block content %}
    <span class="title">
        <h1>{% block title %} Questions {% endblock %}</h1>
    </span>
    <div class="questions">
        <h2>Questions Blueprint</h2>

        <div class="question">
            <div class="new-question">
                <form method="POST">
                    <p>
                        <textarea id="q-content"
                                name="content"
                                placeholder="Question"
                                cols="30" rows="3"></textarea>
                    </p>
                    <textarea id="q-answer"
                            name="answer"
                            placeholder="Answer"
                            cols="30" rows="3"></textarea>
                    <p><input type="submit"></p>
                </form>
            </div>
            <div class="questions-list">
                {% for question in questions %}
                    <div class="question">
                        <h4>{{ question.content }}</h4>
                        <p>{{ question.answer }}</p>
                        <hr>
                    </div>
                {% endfor %}
            </div>
        </div>

    </div>
{% endblock %}
```
flask_app/app/templates/questions/index.html

Save and close the file.

Here, you create a form with two text areas: one for the question’s content and one for its answer. Then you add a submit button for the form.

Below the form, you loop through the ```questions``` variable you passed from the questions’ index route, displaying each question’s content and answer.

With your development server running, use your browser to navigate to the questions index page (**Note**: You may have to restart the server):

```
http://127.0.0.1:5000/questions/
```

The page will load with the blueprint heading, the submission form, and two sample questions:

![image](https://github.com/user-attachments/assets/75f763ab-5c56-42b6-a7de-9caa1823cfa3)





MORE