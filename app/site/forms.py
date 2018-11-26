"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, TextAreaField, IntegerField, \
    SelectMultipleField, FileField
from wtforms.validators import InputRequired, Email, Length, DataRequired, NumberRange, EqualTo
from flask_security import RegisterForm


# The happy-cobra form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter a valid email'), Length(max=60)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)])
    remember = BooleanField('Remember me')


class ExtendedRegisterForm(RegisterForm):
    firstname = StringField('First Name', [DataRequired()])
    lastname = StringField('Last Name', [DataRequired()])


# Account registration  form
class RegisterForm(FlaskForm):
    # email = StringField('Email', validators=[InputRequired(), Email(message='Enter a valid email'), Length(max=60)])
    # password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)])
    firstname = StringField('Firstname', validators=[InputRequired(), Length(max=20)])
    lastname = StringField('Lastname', validators=[InputRequired(), Length(max=20)])


# recover username/password
class RecoverPassForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter a valid email'), Length(max=60)])


# reset password form
class PassResetForm(FlaskForm):
    password = PasswordField('New password', validators=[InputRequired(), Length(min=8, max=30),
                                                         EqualTo("password_repeat",
                                                                 message="Both passwords have to match")])
    password_repeat = PasswordField('Confirm new password', validators=[InputRequired(), Length(min=8, max=30)])


class PassResetForm2(FlaskForm):
    old_pass = PasswordField('Old password', validators=[InputRequired(), Length(min=8, max=30)])
    password = PasswordField('New password', validators=[InputRequired(), Length(min=8, max=30),
                                                         EqualTo("password_repeat",
                                                                 message="Both passwords have to match")])
    password_repeat = PasswordField('Confirm new password', validators=[InputRequired(), Length(min=8, max=30)])

