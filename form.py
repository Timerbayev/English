from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from datetime import date
from wtforms.widgets import TextArea


class DictionaryWords(FlaskForm):
    eng = StringField('English', [DataRequired()])
    rus = StringField('Russia', [DataRequired()])
    text = TextAreaField('Story', render_kw={"rows": 7, "cols": 50})
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    firstname = StringField('Name', [DataRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), Length(min=8, max=20)])
    data = DateField('Data', validators=[DataRequired()], default=date.today())
    submit = SubmitField('Submit')


class Logins(FlaskForm):
    login = StringField('Login', [DataRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password')
    submit = SubmitField('Submit')
