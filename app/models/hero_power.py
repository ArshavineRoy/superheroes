from .db_config import db

class HeroPower(db.Model):

    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    def validate_strength(strength):
        allowed_strengths = ['Strong', 'Weak', 'Average']
        if strength not in allowed_strengths:
            return False
        return True