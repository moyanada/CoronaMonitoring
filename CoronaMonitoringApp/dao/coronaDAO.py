from CoronaMonitoringApp import db
from CoronaMonitoringApp.models import TBL_TEMP_CORONA

def schCoronaDataAll():
    #TBL_TEMP_CORONA.query.filter(TBL_TEMP_CORONA.test_seq==1).all()
    #TBL_TEMP_CORONA.query.filter(TBL_TEMP_CORONA.col1.like('%111%')).all()
    return TBL_TEMP_CORONA.query.all()

def insertSave():
    t = TBL_TEMP_CORONA(temp_seq=2, col1='333', col2='444',col4='555')    
    db.session.add(t)
    db.session.commit();