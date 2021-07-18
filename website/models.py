from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(20000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(16))
    username = db.Column(db.String(150))
    notes = db.relationship('Note')

class PRODUCTS(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer,db.ForeignKey('user.id'))
    PROD_NAME = db.Column(db.String(124))
    KCAL = db.Column(db.Float)
    PROTEIN = db.Column(db.Float)
    FAT = db.Column(db.Float)
    CARB = db.Column(db.Float)

class PROD_UNITS(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    UNIT_DESC = db.Column(db.String(48))

class DAIRY(db.Model):
     ID = db.Column(db.Integer, primary_key=True)
     USER_ID = db.Column(db.Integer,db.ForeignKey('user.id'))
     DATE = db.Column(db.DateTime(timezone=True))
     PROD_ID = db.Column(db.Integer,db.ForeignKey('products.id'))
     AMOUNT = db.Column(db.Float)
     UNIT = db.Column(db.Integer,db.ForeignKey('prod_units.id'))