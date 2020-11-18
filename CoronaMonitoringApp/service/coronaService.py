

def doSaveCoronaData(pStartDt, pEndDt):
    return ''

def getPublicDataCorona(pStartDt, pEndDt):
    import requests
    from bs4 import BeautifulSoup

    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=RsZHhDtUtdHEE4KS2%2FQrBFyxSmwyLUBqdcLdB85Buyr9UXVarWcw8u72p%2F%2FZm%2BkJhpYO%2FGB5348VRg%2BI2MDsHQ%3D%3D'
    paramDict = {        
        "pageNo" : "1"
        ,"numOfRows" : "10"
        ,"startCreateDt" : "20200310"
        ,"endCreateDt" : "20200315"
    }

    response = requests.get(url, params=paramDict)
    soup = BeautifulSoup(response.content, 'lxml-xml')

    if response.status_code == 200:
        resResultCode = soup.find('resultCode').getText()
        resResultMsg = soup.find('resultMsg').getText()
        resXmlItem = soup.find_all('item')

        if resResultCode == '00':
            if len(resXmlItem) > 0:
                print("파실할 데이터 갯수 [{}]".format(len(resXmlItem)))
                for item in resXmlItem:
                    print(item.find('accDefRate').getText())
            else :
                print("파싱할 데이터가 없습니다")
        else :
            print("response Error Code[{}] Msg[{}]".format(resResultCode, resResultMsg))        
    else :
        print("http error {}".format(response.status_code))

    
    