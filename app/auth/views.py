from flask import render_template, session, redirect, flash, url_for
from app.forms import LoginFrom
from . import auth


@auth.route('/login', methods = ['GET','POST'])
def login():
    Login_From = LoginFrom()
    context = {
        'Login_From': Login_From
    }
    
    if Login_From.validate_on_submit():
        username = Login_From.username.data
        session['username'] = username
        # Flash para hacer alertas usando - bootstrap y  javaScritp
        flash('Nombre usuarios registrado con exito')
        return redirect(url_for('index'))
    return render_template('login.html', **context)