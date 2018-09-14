import random

class assemreturn:
    def __init__(self,finish,func):
        self.finish=finish
        self.func=func

addr={
    'map':[]
}
database=[]
target='c'
parameter=['a','v']
finish=False

def assem(tar):
    nofunc=False
    global finish
    def sortfunction(tar):
        
        tar=str(tar)
        cache=[]
        for i in database:
            if i[2]==tar:
                cache.append(i)

        addr.clear()
        addr['map']=[]
        count=0
        for i in cache:
            for j in i[1]:
                if j in parameter:
                    count+=1
            i[3]=count/len(parameter)
            addr['map'].append(float(i[3]))
            addr[float(i[3])]=i
        if addr['map']==[]:
            nofunc=True
        addr['map'].sort()

    func=''
    sortfunction(tar)
    for i in addr['map']:
        if i!=1.0:
            usepara=[]
            cache=[]
            count=0
            for j in addr[i][1]:
                if j not in parameter:
                    cache.append(j)
                else:
                    usepara.append(j)
            
            for j in cache:
                '''
                addrcopy=addr
                assem(j)
                addr=addrcopy
                
                if finish:
                ''' 
                para=''
                for k in usepara:
                    if k==usepara[len(usepara)-1]:
                        para+=str(k)                    
                    else:
                        para+=str(k)+','
                cache[count]=str(addr[i][0])+'('+str(assem(j))+','+para+'),'
                count+=1
            if finish:
                for j in cache:
                    func=''
                    func+=j
                    #print(func)
                    return func
        else:
            finish=True
            func=str(addr[i][0])+str(addr[i][1])
            #print(func)
            return func
    print('no solution')


'''
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
        self.para=[[],[]]
        self.out=[[],[]]
        #self.scope=''
        function=''
    
    def copy(self,target):
        self.para=target.para
        self.out=target.out
        self.function=target.function

    def debug(self):
        print(self.name)
        print(self.para)
        print(self.out)

def readfile(filename):
    f=open(filename,'r')
    return str(f.read())

def dataimport():
    raw=readfile('func.txt')
    raw=raw.split('\n')
    print(raw)
    for i in raw:
        database.append(func())
        cache=database[len(database)-1]
        i=i.split(' ')
        cache.name=str(i[0])
        cache.para[0].extend(i[1].split(','))
        cache.para[1].extend(i[2].split(','))
        cache.out[0].extend(i[3].split(','))
        #cache.out[1].extend(i[4].split(','))
'''
database.extend([['add',('a','b'),'c',0],['sub',('a','v'),'b',0]])#[[name,(parameter),output,sortcode]]
addr[0]=database[0]
ans=assem(target)

print(assem(target)[:-1])




    
    
