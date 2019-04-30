import os
import click

from flask import Flask
from blog_mini.settings import config
from blog_mini.extensions import bootstrap,login_manager,db,csrf,moment,migrate
from blog_mini.models import ArticleType,Source,User,Menu,ArticleTypeSetting,Follow,BlogView,BlogInfo,\
                             Comment,Article,Plugin
from blog_mini.admin import admin as admin_blueprint
from blog_mini.auth import auth as auth_blueprint
from blog_mini.main import main as main_blueprint


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog_mini')
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    moment.init_app(app)
    migrate.init_app(app,db)
    register_shell_context(app)
    register_templates_context(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, ArticleType=ArticleType, Source=Source,
                    Comment=Comment, Article=Article, User=User, Menu=Menu,
                    ArticleTypeSetting=ArticleTypeSetting, BlogInfo=BlogInfo,
                    Plugin=Plugin, BlogView=BlogView)


def register_templates_context(app):
    from blog_mini.models import ArticleType, article_types, Source, \
    Comment, Article, User, Menu, ArticleTypeSetting, BlogInfo, \
    Plugin, BlogView

    app.jinja_env.globals['ArticleType'] = ArticleType
    app.jinja_env.globals['article_types'] = article_types
    app.jinja_env.globals['Menu'] = Menu
    app.jinja_env.globals['BlogInfo'] = BlogInfo
    app.jinja_env.globals['Plugin'] = Plugin
    app.jinja_env.globals['Source'] = Source
    app.jinja_env.globals['Article'] = Article
    app.jinja_env.globals['Comment'] = Comment
    app.jinja_env.globals['BlogView'] = BlogView


def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

def register_commands(app):
    @app.cli.command()
    def forge():
        click.echo('raise data ing...')
        db.drop_all()
        db.create_all()
        # step_1:insert basic blog info
        BlogInfo.insert_blog_info()
        # step_2:insert admin account
        User.insert_admin(email='jjj@126.com', username='jjj', password='123')
        # step_3:insert system default setting
        ArticleTypeSetting.insert_system_setting()
        # step_4:insert default article sources
        Source.insert_sources()
        # step_5:insert default articleType
        ArticleType.insert_system_articleType()
        # step_6:insert system plugin
        Plugin.insert_system_plugin()
        # step_7:insert blog view
        BlogView.insert_view()

        # step_1:insert navs
        Menu.insert_menus()
        # step_2:insert articleTypes
        ArticleType.insert_articleTypes()
        # step_3:generate random articles
        Article.generate_fake(100)
        # step_4:generate random comments
        Comment.generate_fake(300)
        # step_5:generate random replies
        Comment.generate_fake_replies(100)
        # step_4:generate random comments
        Comment.generate_fake(300)

