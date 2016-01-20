import urllib  
import
import cookielib
headers = {
'Accept':'*/*',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'566',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'_ga=GA1.3.548295607.1450860734; Hm_lvt_444bf10f6d7469654b7f41f9f9f9c301=1449989162,1449989164,1451806133,1452091199; ASP.NET_SessionId=khpgrmdvldlapui3h12dbbu1',
'Host:xk.shu.edu.cn:8080',
'Origin':'http://xk.shu.edu.cn:8080',
'Referer':'http://xk.shu.edu.cn:8080/CourseSelectionStudent/FastInput',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2552.0 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}
import urllib2

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()