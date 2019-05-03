from basePageProcess import basePageProcess


class pageprocess(basePageProcess):

    def __init__(self):
        super().__init__()
        self.name = 'python'  # 用于指定调用哪个页面处理程序


    # 调用父类同名方法
    #basePageProcess.process(self,html, bsobj, pageurl, level)
    # 这样做有一些缺点，比如说如果修改了父类名称，那么在子类中会涉及多处修改，
    def process(self, html, bsobj, pageurl, level):
        input = bsobj.find('div',{'class':'article-intro'}).get_text()
        input = self.cleaner.ngram(input)
        input = self.cleaner.stdata(input)
        print(input)
        # super(pageprocess, self).process(html, bsobj, pageurl, level)
