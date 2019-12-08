
import requests
import time
import re


def remove(htmltext, word):
    text = htmltext[:]
    while text.find(word) != -1:
        a = text.find(word)
        text = text[:a]+text[a+len(word):]
    return text


def catchData(word):
    headers = {
        'Host': 'hm.baidu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
'Accept': 'image/webp,*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    }
 
    newUrl = "https://fanyi.baidu.com/?aldtype=16047#en/zh/"+word
    # 最简单的爬虫请求.也可以加上headers字段，防止部分网址的反爬虫机制
    response = requests.get(newUrl, headers=headers)
    #response = requests.get(newUrl)
    # 当爬取的界面需要用户名密码登录时候，构建的请求需要包含auth字段
    #response = requests.get(newUrl,headers=headers,auth=('username','passsword'))
    html = response.content.decode("utf-8")
    # print(html)  # 打印网页内容
    r=re.search("\<div class=\"dictionary\-comment\"\>(.*?)\<\/div\>",html,re.DOTALL)
    # if r:
    #     t = (r.group(2))
    #     t = remove(t, '<li>')
    #     t = remove(t, '</li>')
    #     # t = remove(t, '<span>')
    #     # t = remove(t, '</span>')
    #     t = list(t)
    #     n = ""
    #     for i in t:
    #         if i not in (" ",):
    #             n += i
    # else:
    #     n = html
    n=""
    print(html)
    return n


    # print(response.status_code)#浏览器返回的错误码，200表示成功
f = input("请输入要查找的字词（中间请用逗号隔开）：")
wordList = f.split(",")
ysList = []
for i in wordList:
    ysList.append(catchData(i))
    # print(ysLint[len(ysList)-1])
    # time.sleep(0.5)

n = ""
for i, j in zip(wordList, ysList):
    n += i+":"+j+"\n\n"

print(n)
f = open('out.txt', 'w')
f.write(n)
f.close()
