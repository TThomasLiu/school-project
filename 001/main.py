
database=[]

class var():
    def __init__(self):
        self.group=[]
        self.value=0
        self.type=''

    def checkgroup(self,group):
        return group in self.group

class func():
    
    def __init__(self):
        self.name=''
        self.para=[]
        self.out=[]
        self.scope=''
        function=''
    
    def copy(self,target):
        self.para=target.para
        self.out=target.out
        self.function=target.function

def readfile(filename):
    f=open(filename,'r')
    return str(f.read())

def dataimport():
    raw=readfile('func.txt')

'''
database=[func()]
database[0].para.append('a')
database[0].out.append('b')
database[0].function='b=2*a'
'''

cache=func()
cache.copy(database[0])
print(cache.function)