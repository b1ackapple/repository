import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

key = 'ServiceKey=ta7gZ94tFMtie5Rh4z%2FpKw%2FHatqGXGMdIHqHiGk5%2FFO7H3sOkPMdTtmmH0VrW66AmLYf0aKbyJUnchmulaPGug%3D%3D&'## 서비스키
pageNo = 'pageNo=1&' ##페이지
numOfRows = 'numOfRows=10&'
startDate = int(input("데이터 시작일 입력: (yyyymmdd) !20200320이")) ## 데이터 시작일
enddate= int(input("데이터 종료일 입력: (yyyymmdd)")) # 데이터 종료일
Date_list = []
Chnum = []
while startDate<enddate+1: ## 데이터 마지막
    Date_list.append(startDate)

    startCreateDt = 'startCreateDt='+str(startDate)+'&'
    endCreateDt = 'endCreateDt='+str(startDate)+'&'
    Nationname = []
    Def = []
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?' + key + pageNo + numOfRows + startCreateDt + endCreateDt
    req = requests.get(url) #req<-url
    html = req.text #html<-req
    soup = BeautifulSoup(html, 'html.parser') #soup<-html

    Nn = soup.find_all('nationnm')
    ND = soup.find_all('natdefcnt')
    for st in Nn:
        Nationname.append(st.text)
    for st in ND:
        Def.append(st.text)


    CHN_index = Nationname.index('중국')
    Def[CHN_index] = int(Def[CHN_index]) ## CHN_index: string -> int
    Chnum.append(Def[CHN_index])
    startDate += 1
CHINA_COV = pd.Series(Chnum, index=Date_list)
print(CHINA_COV)
plt.plot(Date_list, Chnum)
plt.title("CHINA_COV19")
plt.xlabel("Date")
plt.ylabel("Def")
plt.show()