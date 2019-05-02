import requests
from bs4 import BeautifulSoup
import re
from distributer import distributer
import string
# coding=gbk

class clawer(object):

    def __init__(self, homepage, prefix):
        self.prefix = prefix
        self.homepage = homepage
        self.distributer = distributer()

    def html(self, pageurl):
        session = requests.Session()
        header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        req = session.get(self.homepage + pageurl, headers=header)
        req.encoding='utf-8'
        return  req.text

    def getlinks(self, pageurl, maxlevel=1):
        html = self.html(pageurl)
        bsobj = BeautifulSoup(html)
        self.distributer.distribute(html, bsobj, pageurl, maxlevel)
        maxlevel -= 1
        if maxlevel >= 0:
            links = bsobj.findAll("a", href=re.compile("^(/"+self.prefix+"/)"))
            for link in links:
                if 'href' in link.attrs:
                    newpage = link.attrs['href']
                    self.getlinks(newpage, maxlevel)
        return
