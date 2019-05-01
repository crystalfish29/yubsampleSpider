#定义一个分发器
class distributer(object):

    def __init__(self):
        self.pageProcesses = []
    #分发信息
    def distribute(self, html, bsobj, pageurl, level):
        for process in self.pageProcesses:
            process.process(html, bsobj, pageurl, level)

    #注册页面处理程序
    def registPageProcess(self, pageprocess):
        self.pageProcesses.append(pageprocess)
