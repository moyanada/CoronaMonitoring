from flask import Blueprint
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for

from CoronaMonitoringApp.dao import coronaDAO
from CoronaMonitoringApp.models import TBL_TEMP_CORONA
from CoronaMonitoringApp.service import coronaService

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template("index.html");

@bp.route('/saveView')
def saveView():
    return render_template("saveView.html");

@bp.route('/coronaGraph')
def coronaGraph():
    coronaList = coronaDAO.schCoronaDataAll();   

    # for coronaData in coronaList:
    #     print(coronaData.temp_seq)

    return render_template("coronaGraph.html", coronaDataList=coronaList)

@bp.route('/saveCorona', methods=['POST'])
def saveCorona():
    startDt = request.form['startDt']
    endDt = request.form['endDt']

    validate(startDt)
    validate(endDt)

    if startDt > endDt:
        print("종료일이 시작일보다 이전 일 수 없습니다.")
        return render_template("saveView.html");

    coronaService.doSaveCoronaData(startDt, endDt);

    return "<script>alert('데이터 적재 완료'); location.href='http://127.0.0.1:5000';</script>"

@bp.route('/saveGraphImg', methods=['POST', 'GET'])
def saveGraphImg():
    coronaService.doSaveCoronaGraphImg();
    return "<script>alert('그래프 생성 완료'); location.href='http://127.0.0.1:5000';</script>"    

def validate(date_text):
    import datetime

    try:
        datetime.datetime.strptime(date_text, '%Y%m%d')
    except ValueError:
        raise ValueError("날짜 형식에 맞지 않습니다.")