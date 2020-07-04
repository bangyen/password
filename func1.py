import pattern as p 
import dict1 as d
mould="(-({})=({})=({})=({})=({})-)"
pattern=p.pattern
def generate(m):
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
    lll=0
    for i in mm:
        if lll == len(mm):
            break
        o1=i[0]
        o2=i[1]
        o3=i[2]
        o4=i[3]
        o5=i[4]
        mould.format(o1,o2,o3,o4,o5)
        lll+=1
generate("abc")
