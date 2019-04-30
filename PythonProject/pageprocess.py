class pageprocess(object):

    def __init__(self):
        pass

    def process(self, html, bsobj, pageurl, level):
        obj= bsobj.find('div',{'id':'content'}).h1.text
        print(pageurl, "%d" % level, "%s"%obj)
        
