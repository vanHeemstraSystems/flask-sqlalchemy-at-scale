# 500 - Creating Flask Blueprints

== WE ARE HERE : https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#step-4-creating-flask-blueprints ==

In this step, you will create a blueprint for the main routes that will manage the main component of your Flask application, and then you will register the blueprint on your factory function. You’ll create another blueprint each for blog posts, questions, and answers. You’ll add a few routes to each blueprint and render templates for each route with a ```templates``` directory for each blueprint.

At this point in the tutorial, your ```flask_app``` directory structure is as follows (excluding the virtual environment’s directory):

```
.
├── flask_app
    ├── app
    │   └── __init__.py
    ├── config.py
    └── requirements.txt
```

## 100 - Creating the Main Blueprint and Rendering its Templates

See [README.md](./100/README.md)