#from src.database import db
from CoronaMonitoringApp import db

class TBL_TEMP_CORONA(db.Model):
    temp_seq=db.Column(db.Integer, primary_key=True)
    state_dt=db.Column(db.Integer, nullable=True)
    decide_cnt=db.Column(db.Integer, nullable=True)
    clear_cnt=db.Column(db.Integer, nullable=True)
    exam_cnt=db.Column(db.Integer, nullable=True)
    death_cnt=db.Column(db.Integer, nullable=True)
    care_cnt=db.Column(db.Integer, nullable=True)
    resutl_neg_cnt=db.Column(db.Integer, nullable=True)
    acc_exam_cnt=db.Column(db.Integer, nullable=True)
    acc_exam_comp_cnt=db.Column(db.Integer, nullable=True)
    acc_def_rate=db.Column(db.Float, nullable=True)