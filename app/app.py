#!/usr/bin/env python3
import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from models.db_config import db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower
from flask_restx import Api, Resource, Namespace, fields
from flask_marshmallow import Marshmallow

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
ma = Marshmallow(app)

api = Api()
api.init_app(app)

ns = Namespace("api")
api.add_namespace(ns)

@ns.route('/')
class Heroes(Resource):
    def get(self):
        return {"message" : "Welcome Home"}, 200



if __name__ == '__main__':
    app.run(port=5555)
