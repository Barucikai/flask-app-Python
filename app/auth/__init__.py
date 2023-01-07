from flask import Blueprint

#la url_prfix para todas las que inicien con el prefijo de /auth seran ruteadas - y crearemos view - vista 
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Para poder importar las vista aqui abajo
from . import views