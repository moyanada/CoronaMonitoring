#from src.database import db
from CoronaMonitoringApp import db

class TBL_TEMP_004(db.Model):
    temp_seq=db.Column(db.Integer, primary_key=True)
    col1=db.Column(db.String(100), nullable=True)
    col2=db.Column(db.String(100), nullable=True)
    col3=db.Column(db.String(100), nullable=True)
    col4=db.Column(db.String(100), nullable=True)