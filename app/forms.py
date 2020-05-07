from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.validators import *
from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
    email = EmailField("E-Mail", validators=[DataRequired()])
    login = StringField('NickName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), PasswordValidator()])
    password_again = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), PasswordValidator(), RepeatPasswordValidator(password)]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    login = StringField('NickName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
