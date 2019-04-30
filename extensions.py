from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_moment import Moment


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()
moment = Moment()


# login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

