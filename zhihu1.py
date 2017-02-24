#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import urllib2
import re
reload(sys)

sys.setdefaultencoding('utf-8') #输出内容是utf-8 格式

url = "http://daily.zhihu.com/"

#获取网页源码
def getHtml(url):
    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0"}
    request = urllib2.Request(url=url,headers=header) #模拟浏览器进行访问
    response = urllib2.urlopen(request)
    text = response.read()
    return text


#通过解析html解析超链接
def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"') #提高效率
    items = re.findall(pattern,html)
    urls = [] #链接的list
    for item in items:
        urls.append('http://daily.zhihu.com/story/' + item)  # 拼接参数
    return urls

#解析日报内容(标题+正文)
def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern,html)
    # print items[0]
    #匹配文章内容
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)  #re.S匹配换行符
    items_withtag = re.findall(pattern,html)
    for item in items_withtag:
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', item)
        print dd
#去掉正文中间的杂质(标签之类的)


html = getHtml(url)
urls = getUrls(html)
for url in urls:
    try:
        getContent(url)
    except Exception,e:
        print e