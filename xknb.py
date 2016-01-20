#coding: utf-8
import urllib2,re,cookielib
import time
import os
import zlib
import urllib
from PIL import Image
from multiprocessing import Process
def GetDate() :
    return time.strftime('%a, %d %b %Y %X GMT')
xkurl = 'http://xk.shu.edu.cn:8080/'
cj=cookielib.MozillaCookieJar()
ckhandler = urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(ckhandler)
opener.open(xkurl)
def GetASession(cookiejar):
    SessionId=str(cookiejar._cookies['xk.shu.edu.cn']['/']['ASP.NET_SessionId'])
    pat=re.compile('SessionId=(\w+)')
    SessionId=re.search(pat,SessionId).group(1)
    return SessionId
Codeurl='http://xk.shu.edu.cn:8080/Login/GetValidateCode?%20%20+%20GetTimestamp()'
Headers={
    'Origin': 'http://xk.shu.edu.cn:8080',
    'Content-Length': '60',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Host': 'xk.shu.edu.cn:8080',
    'Referer': 'http://xk.shu.edu.cn:8080/',
    'Cache-Control': 'max-age=0',
    'Cookie': '_ga=GA1.3.548295607.1450860734; Hm_lvt_444bf10f6d7469654b7f41f9f9f9c301=1449989162,1449989164,1451806133,1452091199; ASP.NET_SessionId='+GetASession(cj),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2552.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}
Response = opener.open(Codeurl,data=None)
im=Image.open(Response)
im.save('code.jpg')
def Login():
    global xkurl
    global Headers
    global im
    im.show()
    code=raw_input('What did you see?')
    Data = {
        'txtUserName':'15123005',
        'txtPassword':'Laizenan09',
        'txtValiCode':str(code),
    }
    PostData=urllib.urlencode(Data)
    Headers['Content-Length'] = str(PostData.__len__())
    Request=urllib2.Request(xkurl,PostData,Headers)
    LoginResult=opener.open(Request)
    LoginResult_read=LoginResult.read()
    Log = re.search('学生信息',LoginResult_read)
    if Log !=None :
        print '登陆成功'
    else :
        print LoginResult_read
Login()