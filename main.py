from urllib import request
from flask import request, make_response, redirect, render_template, url_for, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginFrom

app = create_app()

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor ']

#se crea el decolador y un nuevo comando - para importa 
@app.cli.command()
def test():
    #Nueva estancia 
    tests = unittest.TestLoader().discover('tests')
    #Run para correr todos los tests 
    unittest.TextTestRunner().run(tests)

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
    response = make_response(redirect('/hello'))
    #ip de User se guarda en una cookie
    #PPRIMERA CLASES - 🆑 #respose.set_cookie('user_ip', user_ip)
    #Responde el index con  la ip de user
    #CLASE 16 # se retorna la ip de usuario secreta con un KEY  - METODO >>> SESSION
    session['user_ip'] = user_ip
    return response

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

@app.route('/base', methods=['GET'])
def base():
    user_ip = session.get('user_ip')
    username = session.get('username')
    contexts = {
        'user_ip' : user_ip,
        'todos' : todos,
       'username': username
    }
    return render_template('base.html', **contexts)
