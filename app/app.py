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

ns = Namespace("/")
api.add_namespace(ns)

class HeroesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Hero
        ordered=True

    id = ma.auto_field()
    name = ma.auto_field()
    super_name = ma.auto_field()

hero_power_schema = HeroesSchema()
hero_powers_schema = HeroesSchema(many=True)

class PowersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Hero
        ordered=True

    id = ma.auto_field()
    name = ma.auto_field()
    super_name = ma.auto_field()

power_schema = PowersSchema()
powers_schema = PowersSchema(many=True)

class HeroPowerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Hero
        ordered=True

    id = ma.auto_field()
    name = ma.auto_field()
    super_name = ma.auto_field()

hero_schema = HeroPowerSchema()
heroes_schema = HeroPowerSchema(many=True)
@ns.route('/heroes')
class Heroes(Resource):

    def get(self):
        heroes = Hero.query.all()

        if not heroes:
            return {
                "error": "Restaurant not found"
            }, 404
        else:
            return heroes_schema.dump(heroes), 200



if __name__ == '__main__':
    app.run(port=5555)
