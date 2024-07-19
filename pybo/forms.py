from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('<내용>은 필수입력 항목입니다.')])
    
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('<제목>은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('<내용>은 필수 입력 항목입니다')])

class UserCreateForm(FlaskForm):
    username = StringField('user id', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('password', validators=[DataRequired(), EqualTo('password2', 'wrong password')])
    password2 = PasswordField('checking password', validators=[DataRequired()])
    email = EmailField('e-mail', [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('user id', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('password', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('내용' , validators=[DataRequired()])