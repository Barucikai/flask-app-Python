from urllib import request
from flask import Flask, request, make_response, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app) #Incializa Bootstrap en Flask
#Creacion de Index

todos = ['Enviar dinero', 'No quiero', 'Envio facturar']

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
    #Nueva respuesta Make_response
    respose = make_response(redirect('/hello'))
    #ip de User se guarda en una cookie
    respose.set_cookie('user_ip', user_ip)
    #Responde el index con  la ip de user
    return respose

@app.route('/Home')
def Home():
    return render_template('principal.html')

@app.route('/hello')
def hello():
    #se mustra la ipe del user que se guardo en la cookies
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }
    return render_template('Hola.html', **context )

@app.route('/base')
def base():
    return render_template('base.html')