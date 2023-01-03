from flask_wtf import FlaskForm #Para formularios #clase17
from wtforms.fields import SearchField, PasswordField, SubmitField #clase17 #los atributos para tomar los datos y BOTON con  - wtf 🤙
from wtforms.validators import DataRequired

#wtf para login y formaularios gunto a validaciones
class LoginFrom(FlaskForm):
    username = SearchField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Envia')

#wtf FIN 