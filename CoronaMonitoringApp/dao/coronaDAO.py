from CoronaMonitoringApp import db
from CoronaMonitoringApp.models import TBL_TEMP_CORONA

def schExistsData(pDate):
    query = db.session.query(TBL_TEMP_CORONA).filter(TBL_TEMP_CORONA.state_dt==pDate).count()
    return query
    
def schCoronaDataAll():    
    return TBL_TEMP_CORONA.query.order_by(TBL_TEMP_CORONA.state_dt.asc()).all()

def insertCoronaData(pTblTempCorona):    
    db.session.add(pTblTempCorona)
    db.session.commit();