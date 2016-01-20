#coding:utf-8
import random
import time
import urllib
import urllib2
import zlib
import winsound
import cookielib
import re
import webbrowser
n=0
url='http://xk.shu.edu.cn:8080/CourseSelectionStudent/CtrlViewOperationResult'
SessionId = 'diosvfpdxqnt3bshoncjsrom'
def bang():
    global url
    global SessionId
    headers = {'Origin': 'http://xk.shu.edu.cn:8080', 'Content-Length': '110', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'X-Requested-With': 'XMLHttpRequest', 'Host': 'xk.shu.edu.cn', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2552.0 Safari/537.36', 'Connection': 'keep-alive', 'Cookie': '_ga=GA1.3.548295607.1450860734; Hm_lvt_444bf10f6d7469654b7f41f9f9f9c301=1449989162,1449989164,1451806133,1452091199; ASP.NET_SessionId=' +SessionId , 'Referer': 'http://xk.shu.edu.cn:8080/CourseSelectionStudent/FuzzyQuery', 'Content-Type': 'application/x-www-form-urlencoded'}
    data= {'stuNo': '15123005', 'IgnorCourseGroup': 'false', 'ListCourseStr': '01014127|1010|0', 'IgnorClassMark': 'false', 'IgnorCredit': 'false'}
    data2='ListCourseStr=01014127%7C1010%7C0&stuNo=15123005&IgnorClassMark=false&IgnorCourseGroup=false&IgnorCredit=false'
    request=urllib2.Request(url,data2,headers)
    response = urllib2.urlopen(request)
    res=response.read()
    res=zlib.decompress(res,zlib.MAX_WBITS|32)
    print res
    susmat = re.search('成功',res)
    errmat = re.search('请输入',res)
    errmat2 = re.search('异常',res)
    contmat= re.search ('已满',res)
    havemat=re.search('已选',res)
    if susmat!= None :
        print '成功选课'
        return True
    else :
        if errmat != None or errmat2 != None:
            print '异常出现拉，赶紧来看看！！'
            return True
        else :
            if contmat !=None :
                print '正常选课中.....'
                return False
            elif havemat != None:
                print '已经选好拉'
                return True

while True :
    ret = bang()
    n += 1
    t=random.uniform(3,4)
    if ret :
        winsound.PlaySound('1.wav',winsound.SND_LOOP)
        break
    time.sleep(t/2)
    print n
    time.sleep(t/2)

