from urllib import request
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
#Creacion de Index

todos = ['Enviar dinero', 'No quiero', 'Envio facturar']

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
@app.route('/hello')
def hello():
    #se mustra la ipe del user que se guardo en la cookies
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }
    return render_template('Hola.html', **context )
