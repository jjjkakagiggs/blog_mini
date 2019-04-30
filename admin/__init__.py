from flask import Blueprint

admin = Blueprint('admin',__name__)

from blog_mini.admin import views
