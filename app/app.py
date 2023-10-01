#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models.db_config import db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555)
