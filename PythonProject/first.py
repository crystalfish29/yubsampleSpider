from  clawer import clawer
from  pageprocess import pageprocess
from urllib.request import urlopen
from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

process = pageprocess()
clawer = clawer(process,"https://www.runoob.com/","python")
clawer.getlinks("python")





