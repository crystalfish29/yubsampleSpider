from clawer import clawer
from pageprocess import pageprocess
from urllib.request import urlopen
from urllib import request
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

ssl._create_default_https_context = ssl._create_unverified_context

clawer = clawer("https://www.runoob.com/", "python")
clawer.distributer.registPageProcess(pageprocess())
clawer.getlinks("python", 1)


# def cleanInput(input): # 数据清洗
#     input = re.sub('\n+', " ", input)
#     input = re.sub(' +', " ", input)
#     cleaninput = []
#     input = input.split(' ')
#     for item in input:
#         item = item.strip(string.punctuation)
#         cleaninput.append(item)
#     return cleaninput


# def input(input, n=2):
#     input = cleanInput(input)  # list
#     output = []
#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     return output


# html = urlopen(
#     'https://baike.baidu.com/item/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91/1232539?fr=aladdin')
# bsObj = BeautifulSoup(html)
# # 获取text 内容
# content = bsObj.find('div', {'class': "content"}).get_text()
# ngram = input(content)
# sort = sorted(ngram, key=lambda t: t[1], reverse=True)
# ngram = OrderedDict(sort) 
# for item in ngram:
#     print(item)
#     print(ngram[item])
#     print("\n")
#     print("---------")

#print(ngram)
