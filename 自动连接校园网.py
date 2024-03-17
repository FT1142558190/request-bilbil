from time import sleep
from subprocess import run, PIPE
import datetime, requests, base64
name='202214680507'
password='3d035815d15c15483c7862557262254856925cceea82335f5808fa18027384e04e5672b869b230cea0f95dea35c41818f7c09e4137533f75b6beea490f6fbf630ffd301eaf4343fe5dfee64b43381094ca8580a6a5d4b9ab5a69f19be7bb6549f15fa2c1e94a5d933cea2d9cb3fd46a644af019c03e8ed3d7cc278e955b22888'
servers='%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF'
queryString='wlanuserip%3D5b6b0a7b3c2a48518070a50b7c71e077%26wlanacname%3Dcee24f8cac61aac974e74b503c3a1669%26ssid%3D%26nasip%3D8618724f96768bd61edb375c4c21ccc0%26snmpagentip%3D%26mac%3D403ba52fd6ad7f6a4ac35cd65d199659%26t%3Dwireless-v2%26url%3Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%26apmac%3D%26nasid%3Dcee24f8cac61aac974e74b503c3a1669%26vid%3D5408d730f6b766e8%26port%3Da13f0bc34ff8d655%26nasportid%3D85280d0376cea3452b05fa8dbd58b040e20a0022ec633df36b1e654406b9e3c03574460028a456ea'
LOGIN_PAGE_URL = "http://172.30.0.11/eportal/InterFace.do?method=login"
r = run('ping www.baidu.com',
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE,
        shell=True)
cnt = 1
data1 = {
        "userId": name,
        "password": password,
        "queryString:":queryString,
        'service':servers,
        "passwordEncrypt":'true',
        "operatorPwd": '',
        'operatorUserId':'',
        'validcode':'',
}
header= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'
}
def login():
    requests.post(LOGIN_PAGE_URL, data1, headers=header, json=None)
# while True:
#     if r.returncode:
#         print('relogin 第{}次'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         login()
#         cnt += 1
#     else:
#         print('成功')
#         pass
#     sleep(1)
requests.post(LOGIN_PAGE_URL,data=data1,headers=header,json=None)

# 函数1：测试网络是否连通
# import socket

#
# def is_net_ok():
#     s = socket.socket()
#     s.settimeout(3)
#     try:
#         status = s.connect_ex(('www.baidu.com', 443))
#         if status == 0:
#             s.close()
#             return True
#         else:
#
#             return False
#     except Exception as e:
#         return False



