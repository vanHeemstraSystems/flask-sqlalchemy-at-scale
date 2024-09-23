#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('posts', __name__)

from app.posts import routes