# 200 - Creating and Interacting with the Post Model

In large applications, you may have hundreds of database tables, which means you would need to write hundreds of SQLAlchemy models to manage them. Putting all your models in one file will make your application hard to maintain, so you will split your models into separate Python files inside a models directory. Each file will hold the models and functions related to a specific part of your application. For example, you may put models and functions for managing posts inside a post.py file in a directory called models in the app directory.

At this point in the tutorial, your flask_app directory structure is as follows (excluding the virtual environment’s directory):

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

**Note**: The ```db.create_all()``` function does not recreate or update a table if it already exists. For example, if you want to modify your model by adding a new column and so you run the ```db.create_all()``` function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the ```db.drop_all()``` function and then recreate them with the ```db.create_all()``` function like so:

```
>>> db.drop_all()
>>> db.create_all()
```

These commands will apply the modifications you make to your models and will delete all the existing data in the database. To update the database and preserve existing data, you’ll need to use *[schema migration](https://en.wikipedia.org/wiki/Schema_migration)*, which allows you to modify your tables and preserve data. You can use the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) extension to perform SQLAlchemy schema migrations through the Flask command-line interface.

Next, run the following code to create ten random posts:

```
>>> from app.extensions import db 
>>> from app.models.post import Post
>>> import random
>>>
>>> for i in range(0, 10):
>>>    random_num = random.randrange(1, 1000)
>>>    post = Post(title=f'Post #{random_num}',
>>>                content=f'Content #{random_num}')
>>>    db.session.add(post)
>>>    print(post)
>>>    print(post.content)
>>>    print('--')
>>>    db.session.commit()
```

You import the ```db``` database object, the ```Post``` database model, and the ```random``` Python module. You’ll use this module to generate random numbers to create sample posts with different titles and contents. You use a ```for``` loop with the ```range()``` Python function to repeat a code block ten times.

In the ```for``` loop, you use the ```random.randrange()``` method to generate a random integer number between ```1``` and ```1000``` and save it to a variable called ```random_num```. You then create a post object using the ```Post``` model and use the random number in the ```random_num``` variable to generate a sample post title and content.

You then add the post object to the database session, print the object itself and its content, and commit the transaction.

You’ll receive an output similar to the following but with different numbers:

```
<Post "Post #923">
Content #923
--
<Post "Post #245">
Content #245
--
<Post "Post #124">
Content #124
--
<Post "Post #282">
Content #282
--
<Post "Post #130">
Content #130
--
<Post "Post #650">
Content #650
--
<Post "Post #763">
Content #763
--
<Post "Post #282">
Content #282
--
<Post "Post #423">
Content #423
--
<Post "Post #899">
Content #899
--
```

Each post has a randomly generated number attached to it. These posts will now be in your database.

Leave the Flask shell running and open a new terminal window. Source your environment and navigate to your application folder.

Now that you have some sample posts in your table, you can display them on the posts’ index page. First, open the posts routes file to modify the index route:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/posts/routes.py
```

Edit the imports and the index route as follows:

```
#!/usr/bin/env python
from flask import render_template
from app.posts import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')    
```
flask_app/app/posts/routes.py

Save and close the file.

You import the ```db``` database object and the ```Post``` model. You get all the posts in the database and then pass them to the posts’ index template.

Open the posts’ index template for modification to display the posts you passed to it:

```
(.venv) gitpod /workspace/flask-sqlalchemy-at-scale/flask_app (main) $ nano app/templates/posts/index.html
```

Edit the file as follows:

```
{% extends 'base.html' %}

{% block content %}
    <span class="title"><h1>{% block title %} The Posts Page {% endblock %}</h1></span>
    <div class="content">
        <h2>This is the posts Flask blueprint</h2>
        {% for post in posts %}
            <div class="post">
                <p><b>#{{ post.id }}</b></p>
                <p class="title">
                    <b>
                        <a href="#">
                            {{ post.title }}
                        </a>
                    </b>
                </p>
                <div class="content">
                    <p>{{ post.content }}</p>
                </div>
                <hr>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```
flask_app/app/templates/posts/index.html

Save and close the file.

Here, you loop through posts and display each post’s ID, title, and content.

With the development server running, visit the posts’ index page or refresh it if you have it open:

```
http://127.0.0.1:5000/posts/
```

The sample posts you’ve generated will be displayed on the index page, similar to the following image:

![image](https://github.com/user-attachments/assets/f7ee1c22-0c36-4fcf-b5cd-1a259e0bd05b)

You now have a database model for posts. You can now add features to your application with new routes and templates, such as creating, editing, and deleting posts.