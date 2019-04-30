from flask import Blueprint

main = Blueprint('main',__name__)

from blog_mini.main import views
