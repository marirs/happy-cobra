"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
from werkzeug.security import check_password_hash

from app import db
from uuid import uuid4
from flask_security import RoleMixin

from flask_login import UserMixin

from datetime import datetime

# many-to-many relationship between Users and Roles
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    """Roles
    """
    __tablename__ = 'role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        """enable human-readable values for the Role when editing a User
        if __str__ does not work, try __unicode__ (py 2.7 perhaps)
        """
        return self.name

    def __hash__(self):
        """required to avoid the exception
        TypeError: unhashable type: 'Role' when saving a User
        """
        return hash(self.name)


class User(UserMixin, db.Model):
    """Users
    """
    __tablename__ = 'user'

    id = db.Column(db.String(32), default=lambda: str(uuid4().hex), primary_key=True)
    email = db.Column(db.String(60), unique=True)
    active = db.Column(db.Boolean())
    password = db.Column(db.String(120))
    firstname = db.Column(db.String(20), unique=False)
    lastname = db.Column(db.String(20), unique=False)
    created_date = db.Column(db.DateTime(), unique=False, default=datetime.utcnow())
    email_confirmed = db.Column(db.String(20), unique=False, default='False')

    last_login_ip = db.Column(db.String(18), unique=False)
    current_login_ip = db.Column(db.String(18), unique=False)
    last_login_at = db.Column(db.DateTime, unique=False)
    current_login_at = db.Column(db.DateTime, unique=False)
    login_count = db.Column(db.Integer(), unique=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    track_logins = db.relationship('TrackLogins', backref='linkeduser', cascade='all,delete')

    def as_dict(self):
        """custom deserializer for complex objects when needed
        """
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def has_role(self, role):
        """return the roles of a logged in user
        """
        return role in self.roles


class TrackLogins(db.Model):
    """Track all user logins
    """
    __tablename__ = 'track_logins'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'), nullable=False)
    user_tz = db.Column(db.String(20), unique=False)
    user_language = db.Column(db.String(30), unique=False)
    user_country_code = db.Column(db.String(20), unique=False)
    user_continent = db.Column(db.String(20), unique=False)
    user_sub_loc = db.Column(db.String(20), unique=False)
    ip_address = db.Column(db.String(20), unique=False)
    browser = db.Column(db.String(80), unique=False)
    browser_version = db.Column(db.String(40), unique=False)
    platform = db.Column(db.String(40), unique=False)
    login_date = db.Column(db.DateTime, unique=False)

    def as_dict(self):
        """custom deserializer for complex objects when needed
        """
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
