list = []
a = 12
#def generate(a):
#    for i in range(a):
#        list.append(i)
#    print(list)


class Generate(object):
    def __init__(self, b):
        self.c = b

    def genarate(self):
        for i in range(a):
            list.append(i)
        return list

lol = Generate(10)
print(lol.genarate())
