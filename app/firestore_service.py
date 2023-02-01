import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)
db = firestore.client()

def get_users():
    return db.collection('users').get()

"""def get_todos(class User(db.Model, UserMixin):
    Model for user accounts.
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String,
                         nullable=False,
                         unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.username))
"""
def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()
