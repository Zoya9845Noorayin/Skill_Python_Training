a="Happy Birthday"
print(a[-4:-7:-1])

#With arg with return
def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
            
    return out
print(convert(input('enter a string:'),''))


with arg without return
def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)      
    
print(convert(input('enter a string:'),''))


#without arg without return
def convert():
    s = input('enter a string:')
    out = ''
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    print(out)

convert()

#without arguments and with return
def convert():
    s = input('enter a string:')
    out = ''
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    return 10

print(convert())



class college:
    cname="GCEM"
    cloc='Hoodi'
s1=college()
print(s1.cname,s1.cloc)
print(college.cname)

college.cloc

class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
s1=college('zoya','22229909030','1cshgjb')
s2=college('kashvi','7876879','sdddhihuh')
print(s1.name)
print(s2.name)
s1.display()
s2.display()

