
import os.path

import flask
from flask import request, jsonify
import flask_cors
from flask_sqlalchemy import SQLAlchemy

POSTGRES_USER="vkr"
POSTGRES_PW="vkr"
POSTGRES_DB="eapml"

class VKR(flask.Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CORS позволит нашему фронтенду делать запросы к нашему
        # бэкенду несмотря на то, что они на разных хостах
        # (добавит заголовок Access-Control-Origin в респонсы).
        # Подтюним его когда-нибудь потом.
        flask_cors.CORS(self)

env = os.environ.get('APP_ENV', 'dev')
print(f'Starting application in {env} mode')

app = VKR('vkr')
DB_URL = 'postgresql://{user}:{pw}@postgres/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from backend.models import User

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/add")
def add_user():
    email = request.args.get('email')
    password = request.args.get('password')
    try:
        user = User(
            email = email,
            password = password
        )
        db.session.add(user)
        db.session.commit()
        return "User added. User id = {}, email = {}, password = {}".format(user.id, user.email, user.password)
    except Exception as e:
        return (str(e))

@app.route("/api/v1/users/<int:id_>", methods=["GET"])
def get_by_id(id_):
    try:
        user = User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
        return (str(e))
