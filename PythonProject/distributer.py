# 定义一个分发器
import re


class distributer(object):

    def __init__(self):
        self.pageProcesses = []
    
    # 分发信息 确定是调用哪个页面处理程序
    def distribute(self, html, bsobj, pageurl, level):
        url = self.urlClear(pageurl)
        urlitems = url.split('/')
        if len(urlitems) >= 2:
            flag = urlitems[1]

        for process in self.pageProcesses:
            if process.name in flag:
                process.process(html, bsobj, pageurl, level)
            else:
                continue

    def urlClear(self, pageurl):
        url = re.sub('https://|http://', '', pageurl)
        url = re.sub('//', '/', url)
        return url

    # 注册页面处理程序

    def registPageProcess(self, pageprocess):
        self.pageProcesses.append(pageprocess)
