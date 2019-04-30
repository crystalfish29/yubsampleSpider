from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import re


class clawer(object):

    def __init__(self, homepage, prefix):
        self.prefix = prefix
        self.pageProcesses = []
        self.homepage = homepage

    def registPageProcess(self, pageprocess):
        self.pageProcesses.append(pageprocess)

    def html(self, pageurl):
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        req = request.Request(self.homepage+pageurl, headers=head)
        html = urlopen(req)
        return html

    def getlinks(self, pageurl, maxlevel=1):
        html = self.html(pageurl)
        bsobj = BeautifulSoup(html)
        for item in self.pageProcesses:
            item.process(html, bsobj, pageurl, maxlevel)
        if maxlevel > 0:
            links = bsobj.findAll("a", href=re.compile("^(/"+self.prefix+"/)"))
            maxlevel -= 1
            for link in links:
                if 'href' in link.attrs:
                    newpage = link.attrs['href']
                    self.getlinks(newpage, maxlevel)
        return
