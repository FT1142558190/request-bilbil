# import requests
# import time
# import csv
# import random
# import socket
# import http.client
# import bs4
# from bs4 import BeautifulSoup
#
# def get_content(url,data = None):
#     header = {
#         'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#     }
#     timeout = random.choice(range(80,180))
#     while True:
#         try:
#             rep = requests.get(url,headers =header,timeout = timeout)
#             rep.encoding= 'utf-8'
#             break
#         except socket.timeout as e:
#             print('3:', e)
#             time.sleep(random.choice(range(8, 15)))
#
#         except socket.error as e:
#             print('4:', e)
#             time.sleep(random.choice(range(20, 60)))
#
#         except http.client.BadStatusLine as e:
#             print('5:', e)
#             time.sleep(random.choice(range(30, 80)))
#
#         except http.client.IncompleteRead as e:
#             print('6:', e)
#             time.sleep(random.choice(range(5, 15)))
#     return rep.text
#
# def get_data(html_text):
#     final=[]
#     bs = BeautifulSoup(html_text,"html.parser")  # 创建BS对象
#     body = bs.body
#     data = body.find('div',attrs={'id':'7d'})
#     # data = body.find('div',{'div':'7d'})
#     print(type(data))
#     ul = data.find('ul')
#     li =ul.find_all('li')
#     for day in li:
#         temp = []
#         date = day.find('h1').string
#         temp.append(date)
#         inf = day.find_all('p')
#         temp.append(inf[0].string)
#         if inf[1].find('span') is None:
#             temperature_highest = None
#         else:
#             temperature_highest=inf[1].find('span').string
#             temperature_highestm  =temperature_highest.replace("℃","")
#         temperature_lowest = inf[1].find('i').string
#         temperature_lowest = temperature_lowest.replace('℃','')
#         temp.append(temperature_highest)
#         temp.append(temperature_lowest)
#         final.append(temp)
#     return final
#
# def write_data(data,name):
#     file_name =name
#     with open(file_name,'a',errors='ignore',newline='') as f:
#         f_csv =csv.writer(f)
#         f_csv.writerows(data)
#
# if __name__ == '__main__':
#     url = 'http://www.weather.com.cn/weather/101190401.shtml'
#     html = get_content(url)
#     result = get_data(html)
#     write_data(result,'G:\weather.csv')

import requests
from bs4 import BeautifulSoup

cookie = ''
headers = {
    'cookie': cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'

}


url = "https://space.bilibili.com/2102473659/video"
response = requests.get(url,headers=headers)
html_content = response.text
bs = BeautifulSoup(html_content,"html.parser")
print(html_content)
body = bs.body
data = body.find('div',attrs={'id': "submit-video-list"})

print(data)

# < div id = "submit-video-list"
#
#
# class ="content" > < ul class ="list-list" style="display: none;" > < li data-aid="BV15j41197EH" class ="list-item clearfix fakeDanmu-item" > < a href="//www.bilibili.com/video/BV15j41197EH/" target="_blank" class ="cover" > < div class ="b-img" > < picture class ="b-img__inner" > < source type="image/avif" srcset="//i0.hdslb.com/bfs/archive/b54bd1227819b8ce4717cf65107ea404760c4cde.jpg@320w_200h_1c_!web-space-upload-video.avif" > < source type="image/webp" srcset="//i0.hdslb.com/bfs/archive/b54bd1227819b8ce4717cf65107ea404760c4cde.jpg@320w_200h_1c_!web-space-upload-video.webp" > < img src="//i0.hdslb.com/bfs/archive/b54bd1227819b8ce4717cf65107ea404760c4cde.jpg@320w_200h_1c_!web-space-upload-video.webp" alt="多股细铜线连接做双头usb接口" loading="lazy" onload="bmgOnLoad(this)" onerror="bmgOnError(this)" data-onload="bmgCmptOnload" > < /picture > < /div > < span class ="i-watchlater" > < /span > < !----> < /a > < div class ="c" > < div class ="title-row" > < a href="//www.bilibili.com/video/BV15j41197EH/" target="_blank" title="多股细铜线连接做双头usb接口" class ="title" > 多股细铜线连接做双头usb接口 < /a > < /div > < div title="多股细铜线连接做双头usb接口" class ="desc" >
#