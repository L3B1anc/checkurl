# encoding=utf-8
"""
author:L3b1anc
date:2019.5.13
description:为了检查list中的url是否可以直接访问
"""

import requests
import sys

http = "http"

# 打开txt获取里面的url
def geturl():
    with open("test.txt","r") as urls:
        urls=urls.readlines()
        return urls

#添加http头
def addhttp(url):
    if http in url:
        return url
    else:
        url ="http://"+url
        return url

# 检查url的statuscode
def checkurl(url):
    try:
        print(url)
        r=requests.get(url,verify=False,timeout=3)
        code=r.status_code
        return code
    except requests.exceptions.ConnectTimeout:
        return "链接失败"
    except requests.exceptions.ConnectionError:
        return "链接失败"

#打印结果
def gettxt(name,url):
    name=name+'.txt'
    file=open(name,'a+')
    file.write(url+'\n')
    file.close()


if __name__ == '__main__':
    urls=geturl()
    for url in urls :
        #print(url.replace('\n',''))
        url=url.replace('\n','')
        url=addhttp(url)
        status=checkurl(url)
        # print(status)
        gettxt(str(status),url)
