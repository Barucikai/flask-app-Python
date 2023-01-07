from flask import render_template
from app.forms import LoginFrom
from . import auth


@auth.route('/login')
def login():
    context = {
        'login_from': LoginFrom()
    }
    return render_template('login.html', **context)