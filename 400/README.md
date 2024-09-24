# 400 - Conclusion

You’ve structured a large Flask application using blueprints and organized it with templates and models. You set it up so that each component has its own routes, templates, and models.

The example web application now has three major components that can be expanded upon in different ways:

The main blueprint: You can add an about page or a contact page for users to contact the application owner.

The posts blueprint: You can add pages for creating, editing, deleting, and sorting posts. You can also add tags to posts using a Many-to-Many database relationship with Flask-SQLAlchemy.

The questions blueprint: You can add pages for managing questions and use a One-to-Many database relationship with Flask-SQLAlchemy to create another table for answers so that a question can have multiple solutions.

You can also add more blueprints for features such as authentication, payments, administration, and more.

If you want to read more about Flask, check out the other tutorials in the How To Build Web Applications with Flask series.