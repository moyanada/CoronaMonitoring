from flask import Blueprint


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hellow jun'

@bp.route('/')
def index():
    return 'index page'

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
