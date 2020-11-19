
import matplotlib as mpl
from matplotlib import font_manager as fm
from matplotlib import pyplot as plt
import base64

import io

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

days = ['20200315', '20200314', '20200313', '20200312', '20200311', '20200310']

decideCnt = [8162, 8086 ,7979 ,7869 ,7755 ,7513] #확진자수
clearCnt = [834 ,714 ,510 ,333 ,288 ,247]       #격리해제수
examCnt = [16272 ,17634 ,17940 ,17727 ,18540 ,18452] #검사진행수
deathCnt = [75 ,72 ,67 ,66 ,60 ,54] #사망자수
careCnt = [7253 ,7300 ,7402 ,7470 ,7407 ,7212] # 치료중환자수

resutlNegCnt = [243778 ,235615 ,222728 ,209402 ,196100 ,184179] #결과음성수
accExamCnt = [268212 ,261335 ,248647 ,234998 ,222395 ,210144] #누적검사수
accExamCompCnt = [251940, 243701 ,230707 ,217271 ,203855 ,191692] #누적검사완료수

fig = plt.figure()

plt.plot(days, decideCnt, marker='o')
plt.plot(days, clearCnt, marker='o')
plt.plot(days, examCnt, marker='o')
plt.plot(days, deathCnt, marker='o')
plt.plot(days, careCnt, marker='o')

#plt.plot(days, resutlNegCnt, marker='o')
#plt.plot(days, accExamCnt, marker='o')
#plt.plot(days, accExamCompCnt, marker='o')

#plt.legend(['확진자수', '격리해제수', '검사진행수', '사망자수', '치료중환자수', '결과음성수', '누적검사수', '누적검사완료수'])
plt.legend(['확진자수', '격리해제수', '검사진행수', '사망자수', '치료중환자수'])

plt.xlabel('날짜')
plt.ylabel('숫자(명)')
plt.title('코로나 현황')

plt.show()

#fig.savefig('./test.png', format='png')

# tmpfile = io.BytesIO()
# fig.savefig('/tmp'+tmpfile, format='png')

# encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

# html = 'Some html head' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + 'Some more html'

# with open('test.html','w') as f:
#      f.write(html)