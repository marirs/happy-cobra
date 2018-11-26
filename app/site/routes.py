"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
from flask import Blueprint, render_template, url_for, flash, request
from flask_login.signals import user_logged_in
from flask_security import user_registered

from .. import app
from geoip import geolite2

from app import user_datastore, db
from app.models import TrackLogins, User
from datetime import datetime

site = Blueprint('site', __name__, template_folder='templates')


#
# Error Handlers
#
@app.errorhandler(403)
def not_allowed_here(error):
    message = ['Forbidden', 'You are not allowed to access this page']
    return render_template('error.html', info=message), 403


@app.errorhandler(404)
def page_not_found(error):
    message = ['Page Not Found', 'The page you were looking for is not there. Check if the url is correct.']
    return render_template('error.html', info=message), 404


@app.route('/')
def index():
    return render_template('base.html', title='Home')


#
# Signal Handlers
#
@user_registered.connect_via(app)
def user_registered_sighandler(app, **other_fields):
    """Handler to handle post user registration
    """
    default_role = user_datastore.find_role("User")
    user_datastore.add_role_to_user(other_fields.get('user'), default_role)
    db.session.commit()


@user_logged_in.connect_via(app)
def user_loggedin_sighandler(app, **other_fields):
    """Handler to handle post user logs in
    updates other user happy-cobra details
    """
    user_id = other_fields.get('user').get_id()
    user = User.query.filter_by(id=user_id).first()
    user_tz = ''
    user_country_code = ''
    user_continent = ''
    user_sub_loc = ''

    remote_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    match = geolite2.lookup(remote_ip)

    browser = request.user_agent.browser
    user_language = request.accept_languages[0][0] if len(list(request.accept_languages)) > 0 else ''
    browser_version = request.user_agent.version
    platform = request.user_agent.platform

    if match is not None:
        user_tz = match.timezone
        user_country_code = match.country
        user_continent = match.continent
        user_sub_loc = list(match.subdivisions)[0] if len(list(match.subdivisions)) > 0 else ''

    tracked = TrackLogins(user_tz=user_tz, user_country_code=user_country_code, user_continent=user_continent,
                         user_sub_loc=user_sub_loc, ip_address=remote_ip, browser=browser, user_id=user_id,
                         user_language=user_language, browser_version=browser_version,
                         platform=platform, login_date=datetime.utcnow())
    user.track_logins.append(tracked)
    db.session.commit()
