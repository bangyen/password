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
    mould=mould.format(mm[0][0],mm[0][1],mm[0][2],mm[0][3],mm[0][4])
    mm[0]=mould
    mould=mould.format(mm[1][0],mm[1][1],mm[1][2],mm[1][3],mm[1][4])
    mm[1]=mould
    print(mm)
generate("abc")
