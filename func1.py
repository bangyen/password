import pattern as p 
import dict1 as d

pattern = p.pattern

class Password():
    def __init__(self, m):
        self.m = m
        self.file = ''

    def generate(self):
        global mould
        m = self.m
        m = list(m)
        mm = []
        for index in range(len(m)):
            m[index] = pattern[m[index]]
            mm.append(list(m[index]))
        return mm

    def generate_password(self):
        pp = Password(self.m)
        m = pp.generate()
        mould = "(-({})=({})=({})=({})=({})-)"
        lll = 0
        for i in m:
            if lll == len(m):
                break
            m[lll] = mould.format(*[i[k] for k in range(5)])
            lll += 1
        self.file = m
        return m

    def to_file(self, filename):
        open_file = open(filename, "w")
        for i in self.file:
            open_file.write(i + "\n")


j = Password("abcd")
ll = j.generate_password()
j.to_file("f.txt")
print(ll)
