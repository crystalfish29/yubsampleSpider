from clawer import clawer
from pageprocess import pageprocess
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

clawer = clawer("https://www.runoob.com/", "python")
clawer.distributer.registPageProcess(pageprocess())
clawer.getlinks("python", 1)
