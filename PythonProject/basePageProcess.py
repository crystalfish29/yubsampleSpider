from dataclear import dataclear


class basePageProcess(object):

    def __init__(self):
        self.cleaner = dataclear()
    
    def process(self, html, bsobj, pageurl, level):
        obj = bsobj.find('div', {'id': 'content'}).h1.text
        if level > 0:
            print(pageurl, "\033[1;33m %d \033[0m" % level, "%s" % obj)
        else:
            print(pageurl, "%d" % level, "%s" % obj)
