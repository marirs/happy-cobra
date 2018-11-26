"""
Happy Cobra - Marirs
Skeleton of a Login & Registration system
MIT License
"""
from flask import Blueprint, render_template
from .forms import *
from flask_security import login_required, roles_required, roles_accepted


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/', methods=['GET', 'POST'])
@login_required
@roles_accepted('SuperAdmin', 'Admin')
def admin_index():
    """Admin Index
    """
    return render_template('index.html')
