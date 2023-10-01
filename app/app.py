#!/usr/bin/env python3
import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response
from flask_migrate import Migrate
from models.db_config import db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower

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


@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555)
