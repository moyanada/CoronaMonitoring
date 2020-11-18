from CoronaMonitoringApp.models import TBL_TEMP_004

def schCoronaDataAll():
    return TBL_TEMP_004.query.all()