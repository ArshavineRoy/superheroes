from db_config import db


class Power(db.Model):

    id = db.Column(db.Integer, primary_key=True)
