import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/result_all.aspx'
req = requests.get(url)
req.encoding='utf-8'
soup = BeautifulSoup(req.text, 'html.parser')
#使用到的功能 soup.find_all('a', {"class":"gt"}) , 輸出資料為list 在使用list的索引位置找到需要的資料
#strip() 移除空白

date = soup.select("#SL638DDate_new") #日期
first = soup.find_all('td', {"class":"first"})
print('【威力彩】', first[2].text.strip() + '：' + date[0].text.strip()) #開獎日期


print('第1區 依大小順序排列：', end="")
span = soup.find_all('span') #找所有span標籤tag
for spans in range(3,8+1):
    print(span[spans].text, end=" ")
print('第二區：' + span[9].text.strip(), end="")
print('\n第1區 依開出順序排列：',end="")
for spanss in range(10, 15+1):
    print(span[spanss].text, end=" ")

#找span標籤中的index索引位置的功能，方便找到號碼索引位置
# a = 0
# for i in span:
#     print(str(a) + str(i))
#     a +=1

#結果 資料以爬取日期為準
"""
【威力彩】 開獎日期：108 年 12 月 5 日
第1區 依大小順序排列：03 05 15 21 26 28 第二區：06
第1區 依開出順序排列：05 26 21 15 28 03
"""
