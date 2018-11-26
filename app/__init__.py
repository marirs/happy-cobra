"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
import click
from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security, utils
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

from .config import *

from datetime import datetime

#
# Init the Flask App
#
app = Flask(__name__, template_folder='site/templates')
app.config.from_object(DevelopmentConfig)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
Bootstrap(app)

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.site.forms import ExtendedRegisterForm

#
# Flask Security
#
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=ExtendedRegisterForm)

#
# Blueprints
#
from app.site.routes import site
from app.admin.routes import admin
app.register_blueprint(site)
app.register_blueprint(admin, url_prefix='/admin')


#
# Context Processors
#
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


#
# CLI Commands
#
@app.cli.command('create_super')
@click.argument('firstname')
@click.argument('lastname')
@click.argument('email')
def create_superuser(firstname, lastname, email):
    """Create superuser
    """
    import getpass

    try:
        password = getpass.getpass('Enter your password: ')
        while password is '':
            print('Password cannot be blank')
            password = getpass.getpass('Enter your password: ')
        while len(password) < 8:
            print('Password should be 8 or more chars')
            password = getpass.getpass('Enter your password: ')
        hashed_pass = utils.hash_password(password)

        user_datastore.create_user(email=email, password=hashed_pass, firstname=firstname, lastname=lastname,
                                   email_confirmed=True, confirmed_at=datetime.utcnow())
        user_datastore.add_role_to_user(email, 'SuperAdmin')
        db.session.commit()

        print('User created successfully')
    except IntegrityError:
        db.session.rollback()
        print('User with a similar email already exists.')


@app.cli.command('create_roles')
def create_default_roles():
    """Create default roles
    """
    user_datastore.find_or_create_role(name='SuperAdmin', description='Super Administrators')
    user_datastore.find_or_create_role(name='Admin', description='Administrators')
    user_datastore.find_or_create_role(name='User', description='Users')

    db.session.commit()
    print("Default Roles created.")
