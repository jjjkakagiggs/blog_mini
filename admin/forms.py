from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from blog_mini.main.forms import CommentForm


class CommonForm(FlaskForm):
    types = SelectField('博文分类',coerce=int,validators=[DataRequired()])
    source = SelectField('博文来源', coerce=int, validators=[DataRequired()])


class SubmitArticlesForm(CommonForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField('博文内容', validators=[DataRequired()])
    summary = TextAreaField('博文摘要', validators=[DataRequired()])


class ManageArticlesForm(CommonForm):
    pass


class DeleteArticleForm(FlaskForm):
    articleId = StringField(validators=[DataRequired()])


class DeleteArticlesForm(FlaskForm):
    articleIds = StringField(validators=[DataRequired()])


class DeleteCommentsForm(FlaskForm):
    commentIds = StringField(validators=[DataRequired()])


class AdminCommentForm(CommonForm):
    article = StringField(validators=[DataRequired()])


class AddArticleTypeForm(FlaskForm):
    name = StringField('分类名称', validators=[DataRequired(), Length(1, 64)])
    introduction = TextAreaField('分类介绍')
    setting_hide = SelectField('属性', coerce=int, validators=[DataRequired()])
    menus = SelectField('所属导航', coerce=int, validators=[DataRequired()])
# You must add coerce=int, or the SelectFile validate function only validate the int data


class EditArticleTypeForm(AddArticleTypeForm):
    articleType_id = StringField(validators=[DataRequired()])


class AddArticleTypeNavForm(FlaskForm):
    name = StringField('导航名称', validators=[DataRequired(), Length(1, 64)])


class EditArticleNavTypeForm(AddArticleTypeNavForm):
    nav_id = StringField(validators=[DataRequired()])


class SortArticleNavTypeForm(AddArticleTypeNavForm):
    order = StringField('序号', validators=[DataRequired()])


class CustomBlogInfoForm(FlaskForm):
    title = StringField('博客标题', validators=[DataRequired()])
    signature = TextAreaField('个性签名', validators=[DataRequired()])
    navbar = SelectField('导航样式', coerce=int, validators=[DataRequired()])


class AddBlogPluginForm(FlaskForm):
    title = StringField('插件名称', validators=[DataRequired()])
    note = TextAreaField('备注')
    content = TextAreaField('内容', validators=[DataRequired()])


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原来密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='两次输入密码不一致！')])
    password2 = PasswordField('确认新密码', validators=[DataRequired()])


class EditUserInfoForm(FlaskForm):
    username = StringField('昵称', validators=[DataRequired()])
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码确认', validators=[DataRequired()])