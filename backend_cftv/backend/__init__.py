from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cftv.db'
app.config['SECRET_KEY'] = '99d83fddcdd9f2847cb5faa20a2842dd'

db = SQLAlchemy(app)

# CORS(app, resources={r"/*":{'origins': '*', "allow_headers":"Acess-Control-Allow-Origin"}})
CORS(app, resources={r"/*": {'origins': '*', 'allow_headers': ['Content-Type', 'Access-Control-Allow-Origin']}})

from .controller import funcionario_controller
from .controller import video_feed_controller
from .controller import setor_controller
from .controller import treinar_model_controller

with app.app_context():
    db.create_all()

