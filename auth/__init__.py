from flask import Blueprint

auth = Blueprint('auth',__name__)

from blog_mini.auth import views