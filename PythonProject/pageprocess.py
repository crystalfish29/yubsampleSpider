class pageprocess(object):

    
    def __init__(self):
        self.name = 'python' #用于指定调用哪个页面处理程序

    def process(self, html, bsobj, pageurl, level):
        obj= bsobj.find('div',{'id':'content'}).h1.text
        if level >0:
            print(pageurl, "\033[1;33m %d \033[0m" % level, "%s"%obj)
        else:
            print(pageurl, "%d" % level, "%s"%obj)
        
        
