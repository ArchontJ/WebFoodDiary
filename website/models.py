from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(20000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('USER.ID'))

class DAIRY(db.Model):
     ID = db.Column(db.Integer, primary_key=True)
     USER_ID = db.Column(db.Integer,db.ForeignKey('USER.ID'))
     DATE = db.Column(db.DateTime(timezone=True))
     PROD_ID = db.Column(db.Integer,db.ForeignKey('PRODUCTS.ID'))
     AMOUNT = db.Column(db.Float)
     UNIT = db.Column(db.Integer,db.ForeignKey('PROD_UNITS.ID'))

class PROD_UNITS(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    UNIT_DESC = db.Column(db.String(48))
    dairies = db.relationship('Dairy')

class PRODUCTS(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer,db.ForeignKey('USER.ID'))
    PROD_NAME = db.Column(db.String(124))
    KCAL = db.Column(db.Float)
    PROTEIN = db.Column(db.Float)
    FAT = db.Column(db.Float)
    CARB = db.Column(db.Float)
    dairies = db.relationship('Dairy')

class USER(db.Model, UserMixin):
    ID = db.Column(db.Integer, primary_key=True)
    EMAIL = db.Column(db.String(150),unique=True)
    PASSWORD = db.Column(db.String(16))
    USERNAME = db.Column(db.String(150))
    NOTES = db.relationship('Note')
    PRODUCTS=db.relationship('Products')
    DAIRIES = db.relationship('Dairy')