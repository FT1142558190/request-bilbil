import requests
from bs4 import BeautifulSoup

cookie = ''
headers = {
    # 'cookie': cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'

}


url = "https://yisheng.ncst.edu.cn/col/1444815691333/index.html"
response = requests.get(url,headers=headers)
html_content = response.text
bs = BeautifulSoup(html_content,"html.parser")

body = bs.body
data = body.find('div',attrs={})

print(data)
# <div style="width:100%; height:30px; border-bottom:1px dashed #aaccee;">
#   <div style="width:80%; height:30px; float:left; background:url(http://yisheng.ncst.edu.cn/atm/1444871919355/20151015104057300.png) left center no-repeat; padding-left:15px;"><a href="http://yisheng.ncst.edu.cn/col/1444815691333/2023/06/25/1687701260873.html" style="color:#000; font-size:13px; font-family:微软雅黑; line-height:30px; text-decoration:none;">以升创新教育基地开展访企拓岗活动</a></div>
#   <div style="width:15%; height:30px; line-height:30px; float:right; text-align:right;">2023-06-25</div>
# </div>
# <div style="width:80%; height:30px; float:left; background:url(http://yisheng.ncst.edu.cn/atm/1444871919355/20151015104057300.png) left center no-repeat; padding-left:15px;"><a href="http://yisheng.ncst.edu.cn/col/1444815691333/2023/07/07/1688711493867.html" style="color:#000; font-size:13px; font-family:微软雅黑; line-height:30px; text-decoration:none;">以升创新教育基地开展主题教育专题党课</a></div>