
from app.forms import LoginFrom
from . import auth


@auth.route('/login')
def login():
    context = {
        'login_form': LoginFrom()
    }
    return ''