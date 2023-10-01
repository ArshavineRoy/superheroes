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

heroes_schema = HeroesSchema(many=True)

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

hero_power_schema = HeroPowerSchema()
hero_powers_schema = HeroPowerSchema(many=True)



@ns.route('/heroes')
class Heroes(Resource):

    def get(self):
        heroes = Hero.query.all()

        if not heroes:
            return {
                "error": "No heroes not found"
            }, 404
        else:
            return heroes_schema.dump(heroes), 200
        
@ns.route('/heroes/<int:id>')
class HeroesByID(Resource):

    def get(self, id):
        hero = Hero.query.get(id)

        if not hero:
            return {
                "error": "Hero not found"
            }, 404
        else:
            powers = Power.query.join(HeroPower).filter(HeroPower.hero_id == id).all()
                        
            res_body = {
                "id" : hero.id,
                "name" : hero.name,
                "super_name" : hero.super_name,
                "powers" : []
            }

            for power in powers:
                power_details = {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
                }
                res_body["powers"].append(power_details)

            return res_body, 200





if __name__ == '__main__':
    app.run(port=5555, debug=True)
