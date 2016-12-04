# -*- coding: UTF-8 -*-
#需要事先创建vpn连接：1、名为VPN。2、pptp连接方式
#后续需要定时任务，每个整点前一分钟时候自动断开重新连接
from lxml import html
import requests
page = requests.get('http://free.0ff0.net/')
tree = html.fromstring(page.text)
plist = tree.xpath('//span[@class="txt"]/p/text()')
ip= plist[0]
user=plist[1]
page = requests.get('http://139.162.74.217/mm.txt')
passwd = page.text
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
ip=ip[11:(33-8)]
print(ip)
user=user[12:]
print user
passwd=passwd[0:len(passwd)-1]
print passwd
cmd='rasdial "VPN" %s %s /phone:%s' 
import os
newcmd = (cmd %(user.encode('u8'),passwd.encode('u8'),ip.encode('u8')))
print(newcmd)
print type(newcmd)
os.system(newcmd)