
import copy

#define
funcdatabase=[
    ['add',('a','b'),'c',0],
    ['sub',('a','v'),'b',0]
]
chosenfunc=[]
finish=False
#parameter
target='c'
parameter=['a','v']
#function
def assem(layer,tar):
    global finish
    def sortfunc():
        pos=0
        for i in funcdatabase:
            funcdatabase[pos][3]=0
            pos+=1
        chosenfunc.clear()
        for i in funcdatabase:
            if tar in i[2]:
                chosenfunc.append(copy.copy(i))
        pos=0
        for i in chosenfunc:
            count=0
            #print(chosenfunc[pos])
            for j in i[1]:
                for k in parameter:
                    if k in j:
                        count+=1
            chosenfunc[pos][3]=count/len(parameter)
            pos+=1
        chosenfunc.sort

    sortfunc()
    for i in chosenfunc:
        func=''
        #print(i)
        if i[3]!=1.0:
            finish=False
            unknown=[]
            known=[]
            for j in i[1]:
                if j not in parameter:
                    unknown.append(j)
                else:
                    known.append(j)
            #print(chosenfunc)
            func=i[0]+'('
            for j in known:
                func+=str(j)+','        
            for j in unknown:
                func=func+assem(layer+1,j)+','
            func=func[:-1]+')'
            if finish:
                return func
        else:
            finish=True
            return i[0]+str(i[1])

#main
print(assem(0,target))