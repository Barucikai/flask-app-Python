from urllib import request
from flask import Flask, request, make_response, redirect, render_template, url_for, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm #Para formularios #clase17
from wtforms.fields import SearchField, PasswordField, SubmitField #clase17 #los atributos para tomar los datos y BOTON con  - wtf 🤙
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app) #Incializa Bootstrap en Flask
#Creacion de Index
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Enviar dinero', 'No quiero', 'Envio facturar']

#wtf para login y formaularios gunto a validaciones
class LoginFrom(FlaskForm):
    username = SearchField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Envia')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    #En la variable User_ip se Guarda la ip del usuario
    user_ip = request.remote_addr
    #Redirecion de hacia la pestaña de Hello
    #Nueva respuesta Make_responses
    respose = make_response(redirect('/hello'))
    #ip de User se guarda en una cookie
    #PPRIMERA CLASES - 🆑 #respose.set_cookie('user_ip', user_ip)
    #Responde el index con  la ip de user
    #CLASE 16 # se retorna la ip de usuario secreta con un KEY  - METODO >>> SESSION
    session['user_ip'] = user_ip
    return respose

@app.route('/Home')
def Home():
    return render_template('principal.html')

@app.route('/hello')
def hello():
    #se mustra la ipe del user que se guardo en la cookies
    #CLASE 16 # METODO SESSION - KEY IP 
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }
    return render_template('Hola.html', **context )

@app.route('/base', methods=['GET','POST'])
def base():
    user_ip = session.get('user_ip')
    Login_From = LoginFrom()
    username = session.get('username')
    
    contexts = {
        'user_ip' : user_ip,
        'todos' : todos,
       'Login_From': Login_From,
       'username': username
    }
    
    if Login_From.validate_on_submit():
        username = Login_From.username.data
        session['username'] = username
        return redirect(url_for('base'))
    #Flash para hacer alertas usando - bootstrap y  javaScritp
    flash('Nombre usuarios registrado con exito')
        
    return render_template('base.html', **contexts)