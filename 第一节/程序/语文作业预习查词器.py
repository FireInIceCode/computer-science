
import requests
import time
import re

#删除HTML文档中的标签.
#实际功能:将HTMLtext中所有的word删除
def remove(htmltext, word):
    text = htmltext[:]
    while text.find(word) != -1:
        a = text.find(word)
        text = text[:a]+text[a+len(word):]
    return text

#爬取数据
def catchData(word):
    #声明请求头,伪装成浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    #我们要请求的地址
    newUrl = "https://hanyu.baidu.com/s?wd="+word+"+意思&from=zici"
    #获得请求信息
    response = requests.get(newUrl, headers=headers)
    #获取HTML页面
    html = response.content.decode("utf-8")
    #如果这是一个字:
    if len(word) == 1:
        #匹配:
        r = re.search(
            "\<div class\=\"tab\-content\"\>.*?\<dl\>.*?\<dd\>(.*?)<\/dd\>", html, re.DOTALL)
    #否则
    else:
        #另一种匹配
        r = re.search(
            "\<div class\=\"tab\-content\"\>.*?\<dt class\=\"pinyin\"\>.*?\<dd\>(.*?)<\/dd\>", html, re.DOTALL)
    #如果检索到结果:
    if r:
        #获得目标内容
        t = (r.group(1))
        #删除多余标签
        t = remove(t, '<p>')
        t = remove(t, '</p>')
        t = remove(t, '<span>')
        t = remove(t, '</span>')
        #过滤空格
        t = list(t)
        n = ""
        for i in t:
            if i not in (" ", "\n"):
                n += i
    #如果没有匹配到相关内容
    else:
        #没有相关信息
        n = "no file"
    #返回查询结果
    return n



f = input("请输入要查找的字词（中间请用空格隔开）：")
wordList = f.split(" ")

ysList = []
for i in wordList:
    #搜索每一个词语
    ysList.append(catchData(i))
    time.sleep(0.5)

#将结果转换成文本
n = ""
for i, j in zip(wordList, ysList):
    n += i+":"+j+"\n\n"

print(n)

#写入文件
f = open('out.txt', 'w')
f.write(n)
f.close()
