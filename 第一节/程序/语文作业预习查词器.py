
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    newUrl = "https://hanyu.baidu.com/s?wd="+word+"+意思&from=zici"
    # 最简单的爬虫请求.也可以加上headers字段，防止部分网址的反爬虫机制
    response = requests.get(newUrl, headers=headers)
    # 当爬取的界面需要用户名密码登录时候，构建的请求需要包含auth字段
    #response = requests.get(newUrl,headers=headers,auth=('username','passsword'))
    html = response.content.decode("utf-8")
    # print(html)  # 打印网页内容
    if len(word) == 1:
        r = re.search(
            "\<div class\=\"tab\-content\"\>.*?\<dl\>.*?\<dd\>(.*?)<\/dd\>", html, re.DOTALL)
    else:
        r = re.search(
            "\<div class\=\"tab\-content\"\>.*?\<dt class\=\"pinyin\"\>.*?\<dd\>(.*?)<\/dd\>", html, re.DOTALL)

    if r:
        t = (r.group(1))
        t = remove(t, '<p>')
        t = remove(t, '</p>')
        t = remove(t, '<span>')
        t = remove(t, '</span>')
        t = list(t)
        n = ""
        for i in t:
            if i not in (" ", "\n"):
                n += i
    else:
        n = "no file"
    return n


    # print(response.status_code)#浏览器返回的错误码，200表示成功
f = input("请输入要查找的字词（中间请用空格隔开）：")
wordList = f.split(" ")
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
