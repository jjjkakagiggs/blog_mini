from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional

class CommentForm(FlaskForm):
    name = StringField('昵称', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64),Email()])
    content = TextAreaField('内容', validators=[DataRequired(), Length(1, 1024)])
    follow = StringField(validators=[DataRequired()])