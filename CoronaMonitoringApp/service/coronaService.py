from CoronaMonitoringApp.dao import coronaDAO
from CoronaMonitoringApp.models import TBL_TEMP_CORONA

def doSaveCoronaData(pStartDt, pEndDt):
    coronaDataList = getPublicDataCorona(pStartDt=pStartDt, pEndDt=pEndDt)    

    for coronaData in coronaDataList:        
        cnt = coronaDAO.schExistsData(coronaData.state_dt)
        if cnt > 0:
            print("[{}] 데이터가 이미 있습니다".format(coronaData.state_dt))
            pass
        else :
            coronaDAO.insertCoronaData(coronaData)
            print("[{}] 데이터를 저장하였습니다.".format(coronaData.state_dt))




def getPublicDataCorona(pStartDt, pEndDt):
    import requests
    from bs4 import BeautifulSoup

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=RsZHhDtUtdHEE4KS2%2FQrBFyxSmwyLUBqdcLdB85Buyr9UXVarWcw8u72p%2F%2FZm%2BkJhpYO%2FGB5348VRg%2BI2MDsHQ%3D%3D'
    paramDict = {        
        "pageNo" : "1"
        ,"numOfRows" : "10"
        ,"startCreateDt" : pStartDt
        ,"endCreateDt" : pEndDt
    }

    response = requests.get(url, params=paramDict)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    row = []
    if response.status_code == 200:
        resResultCode = soup.find('resultCode').getText()
        resResultMsg = soup.find('resultMsg').getText()
        resXmlItem = soup.find_all('item')

        if resResultCode == '00':
            if len(resXmlItem) > 0:
                print("파실할 데이터 갯수 [{}]".format(len(resXmlItem)))
                for item in resXmlItem:                    
                    t = TBL_TEMP_CORONA(temp_seq=item.find('seq').getText()
                                        ,state_dt=item.find('stateDt').getText()
                                        ,decide_cnt=item.find('decideCnt').getText()
                                        ,clear_cnt=item.find('clearCnt').getText()
                                        ,exam_cnt=item.find('examCnt').getText()
                                        ,death_cnt=item.find('deathCnt').getText()
                                        ,care_cnt=item.find('careCnt').getText()
                                        ,resutl_neg_cnt=item.find('resutlNegCnt').getText()
                                        ,acc_exam_cnt=item.find('accExamCnt').getText()
                                        ,acc_exam_comp_cnt=item.find('accExamCompCnt').getText()
                                        ,acc_def_rate=item.find('accDefRate').getText())
                    row.append(t);

            else :
                print("파싱할 데이터가 없습니다")
        else :
            print("response Error Code[{}] Msg[{}]".format(resResultCode, resResultMsg))        
    else :
        print("http error {}".format(response.status_code))

    return row

    
def doSaveCoronaGraphImg():    
    import matplotlib as mpl
    from matplotlib import font_manager as fm
    from matplotlib import pyplot as plt
    import base64
    import io

    # 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
    mpl.rcParams['axes.unicode_minus'] = False
    plt.rcParams["figure.figsize"]=(5,5)

    coronaList = coronaDAO.schCoronaDataAll();
    days = []
    decideCnt = []
    clearCnt = []
    examCnt = []
    deathCnt = []
    careCnt = []
    # tmp[4:6]+'/'+tmp[6:]
    for coronaData in coronaList:
        days.append(str(coronaData.state_dt)[4:6]+'/'+str(coronaData.state_dt)[6:])
        decideCnt.append(coronaData.decide_cnt)
        clearCnt.append(coronaData.clear_cnt)
        examCnt.append(coronaData.exam_cnt)
        deathCnt.append(coronaData.death_cnt)
        careCnt.append(coronaData.care_cnt)

    fig = plt.figure()           

    plt.plot(days, decideCnt, marker='o', color='red', label='확진자수')
    plt.xlabel('날짜')
    plt.ylabel('숫자(명)')
    plt.title('확진자수 현황')
    plt.legend()
    
    fig.savefig('static/images/1.png', format='png')
    plt.clf()
        
    plt.plot(days, clearCnt, marker='o', color='blue', label='격리해제수')
    plt.xlabel('날짜')
    plt.ylabel('숫자(명)')
    plt.title('격리해제수 현황')
    plt.legend()

    fig.savefig('static/images/2.png', format='png')
    plt.clf()

    plt.plot(days, examCnt, marker='o', color='orange', label='검사진행수')
    plt.xlabel('날짜')
    plt.ylabel('숫자(명)')
    plt.title('검사진행수 현황')
    plt.legend()

    fig.savefig('static/images/3.png', format='png')
    plt.clf()

    plt.plot(days, deathCnt, marker='o', color='red', label='사망자수')
    plt.xlabel('날짜')
    plt.ylabel('숫자(명)')
    plt.title('사망자수 현황')
    plt.legend()

    fig.savefig('static/images/4.png', format='png')
    plt.clf()

    plt.plot(days, careCnt, marker='o', color='orange', label='치료중환자수')
    plt.xlabel('날짜')
    plt.ylabel('숫자(명)')
    plt.title('치료중환자수 현황')
    plt.legend()

    fig.savefig('static/images/5.png', format='png')
    plt.clf()
    
    #plt.legend(['확진자수', '격리해제수', '검사진행수', '사망자수', '치료중환자수'])

    
    
    # plt.show()

    