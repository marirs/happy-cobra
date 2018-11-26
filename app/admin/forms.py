"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, TextAreaField, IntegerField, SelectMultipleField, FileField, SelectField
from wtforms.validators import InputRequired, Email, Length, DataRequired, NumberRange, EqualTo

#The admin happy-cobra form
class AdminLoginForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(),Email(message='Enter a valid email'), Length(max = 60)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)])
    remember = BooleanField('Remember me')

class EditUserForm(FlaskForm):
    firstname = StringField('Firstname',validators=[InputRequired(), Length(max = 20)])
    lastname = StringField('Lastname',validators=[InputRequired(), Length(max = 20)])

