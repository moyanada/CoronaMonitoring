from flask import Blueprint
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

from CoronaMonitoringApp.dao import coronaDAO
from CoronaMonitoringApp.models import TBL_TEMP_CORONA
from CoronaMonitoringApp.service import coronaService

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    coronaList = coronaDAO.schCoronaDataAll();

    for coronaData in coronaList:
        print(coronaData.col1)

    coronaService.getPublicDataCorona("20200301", "20200302");

    return 'hellow jun'

@bp.route('/')
def index():
    return render_template("index.html");

@bp.route('/dbtest')
def dbtest():
    # import cx_Oracle
    # import os
    # os.putenv('NLS_LANG', '.UTF8')

    # LOCATION=r"C:\03_workspace\07_oracle\instantclient_19_8"
    # os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]
    
    # dsn=cx_Oracle.makedsn("10.40.62.167",14766,"SGIFTOD")
    # db=cx_Oracle.connect("BKOMASTER", "BKOMASTER66S#", dsn)

    # cursor=db.cursor()
    # cursor.execute("select cd_nm from cd_pub")
    # #cursor.fetchall()

    # for name in cursor:
    #     print("cd_nm : {}".format(name))


    # cursor.close()
    # db.close()


    return ""

@bp.route('dbtest2')
def dbtest2():
    # from sqlalchemy import create_engine
    # import pandas as pd
    # import cx_Oracle
    # import os
    # os.putenv('NLS_LANG', '.UTF8')

    # LOCATION=r"C:\03_workspace\07_oracle\instantclient_19_8"
    # os.environ["PATH"]=LOCATION+";"+os.environ["PATH"]

    # user='BKOMASTER'
    # pwd='BKOMASTER66S#'
    # dsn=cx_Oracle.makedsn('10.40.62.167',14766,"SGIFTOD")
    # ora_engine=create_engine(f'oracle+cx_oracle://{user}:{pwd}@{dsn}', echo=True)
    # ora_engine.connect()

    # outpt = ora_engine.execute("SELECT CD_NM FROM CD_PUB")
    # df = pd.DataFrame(outpt.fetchall())
    # df.columns = outpt.keys()
    # print(df.head())

    #ora_engine.close();

    return ""
