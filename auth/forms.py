from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email




class LoginForm(FlaskForm):
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('密码', validators=[DataRequired()])