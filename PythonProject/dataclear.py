import re
import string
from collections import OrderedDict


class dataclear(object):

    def __init__(self):
        pass

    def clearData(self, input):
        input = re.sub('\n+', " ", input)
        input = re.sub(' +', ' ', input)

        output = []
        input = input.split(' ')
        for item in input:
            item = item.strip(string.punctuation)
            output.append(item)
        return output

    def ngram(self, input, n=2):
        input = self.clearData(input)  # []
        output = []
        for i in range(len(input)-n+1):
            output.append(input[i:n+i])
        return output

    def stdata(self, input):
        sort = sorted(input, key=lambda t: t[1], reverse=True)
        sort = OrderedDict(sort)
        return sort
