from basePageProcess import basePageProcess


class pageprocess(basePageProcess):

    def __init__(self):
        self.name = 'python'  # 用于指定调用哪个页面处理程序


    # 调用父类同名方法
    #basePageProcess.process(self,html, bsobj, pageurl, level)
    # 这样做有一些缺点，比如说如果修改了父类名称，那么在子类中会涉及多处修改，
    def process(self, html, bsobj, pageurl, level):
        super(pageprocess, self).process(html, bsobj, pageurl, level)
        print("-------------")
