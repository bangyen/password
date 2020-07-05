import pattern as p 
import dict1 as d
pattern=p.pattern
class Password():
    def __init__(self,m):
        self.m=m
        self.file=""
    def generate(self):
        m=self.m
        global mould
        m=list(m)    
        mm=[]
        m_index=0
        for i in m:
            m[m_index]=pattern[m[m_index]]
            m_index+=1
        m_index=0
        for i in range(len(m)):
            li=list(m[i])
            mm.append(li)
        return mm
    def generate_password(self):
        pp=Password(self.m)
        m=pp.generate()
        mould="(-({})=({})=({})=({})=({})-)"
        lll=0
        for i in m:
            if lll == len(m):
                break
            o1=i[0]
            o2=i[1]
            o3=i[2]
            o4=i[3]
            o5=i[4]
            m[lll]=mould.format(o1,o2,o3,o4,o5)
            lll+=1
        self.file=m
        return m
    def to_file(self,filename):
        open_file=open(filename,"w")
        for i in self.file:
            open_file.write(i+"\n")
j=Password("abcd")
ll=j.generate_password()
j.to_file("f.txt")
print(ll)
